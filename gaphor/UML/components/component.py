"""
Component item.
"""

from gaphor import UML
from gaphor.core.modeling.properties import attribute
from gaphor.diagram.presentation import Classified, ElementPresentation
from gaphor.diagram.shapes import Box, EditableText, Text, cairo_state, draw_border
from gaphor.diagram.support import represents
from gaphor.diagram.text import FontWeight, VerticalAlign
from gaphor.UML.classes.stereotype import stereotype_compartments


@represents(UML.Component)
class ComponentItem(ElementPresentation, Classified):
    def __init__(self, id=None, model=None):
        super().__init__(id, model)

        self.watch("show_stereotypes", self.update_shapes)
        self.watch("subject[NamedElement].name")
        self.watch("subject.appliedStereotype", self.update_shapes)
        self.watch("subject.appliedStereotype.classifier.name")
        self.watch("subject.appliedStereotype.slot", self.update_shapes)
        self.watch("subject.appliedStereotype.slot.definingFeature.name")
        self.watch("subject.appliedStereotype.slot.value", self.update_shapes)
        self.watch("subject[Classifier].useCase", self.update_shapes)

    show_stereotypes: attribute[int] = attribute("show_stereotypes", int)

    def update_shapes(self, event=None):
        self.shape = Box(
            Box(
                Text(text=lambda: UML.model.stereotypes_str(self.subject),),
                EditableText(
                    text=lambda: self.subject.name or "",
                    style={"font-weight": FontWeight.BOLD},
                ),
                style={"padding": (4, 34, 4, 4), "min-height": 44},
                draw=draw_component_icon,
            ),
            *(self.show_stereotypes and stereotype_compartments(self.subject) or []),
            style={
                "min-width": 100,
                "min-height": 50,
                "vertical-align": VerticalAlign.TOP
                if self.canvas and self.canvas.get_children(self)
                else VerticalAlign.MIDDLE,
            },
            draw=draw_border
        )

    def postload(self):
        self.update_shapes()
        super().postload()


def draw_component_icon(box, context, bounding_box):
    with cairo_state(context.cairo) as cr:
        fill_color = context.style["background-color"] or (1, 1, 1, 1)
        stroke_color = context.style["color"] or (0, 0, 0, 1)

        cr.set_line_width(1.0)
        icon_height = 20
        icon_width = 16
        icon_margin_x = 6
        ix = bounding_box.width - icon_margin_x - icon_width
        icon_margin_y = 12

        iy = icon_margin_y

        cr.rectangle(ix, iy, icon_width, icon_height)
        cr.set_source_rgba(*stroke_color)
        cr.stroke()

        bar_padding = 4
        bx = ix - bar_padding
        bar_upper_y = iy + bar_padding
        bar_lower_y = iy + bar_padding * 3

        bar_width = 12
        bar_height = 4
        cr.rectangle(bx, bar_lower_y, bar_width, bar_height)
        cr.set_source_rgba(*fill_color)
        cr.fill_preserve()
        cr.set_source_rgba(*stroke_color)
        cr.stroke()

        cr.rectangle(bx, bar_upper_y, bar_width, bar_height)
        cr.set_source_rgba(*fill_color)
        cr.fill_preserve()
        cr.set_source_rgba(*stroke_color)
        cr.stroke()
