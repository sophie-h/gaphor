# This file is generated by coder.py. DO NOT EDIT!
# isort: skip_file
# flake8: noqa F401,F811
# fmt: off

from __future__ import annotations

from gaphor.core.modeling.properties import (
    association,
    attribute as _attribute,
    derived,
    derivedunion,
    enumeration as _enumeration,
    redefine,
    relation_many,
    relation_one,
)


from gaphor.UML.uml import Class
from gaphor.SysML.sysml import Block
class Situation(Block, Class):
    pass


from gaphor.SysML.sysml import DirectedRelationshipPropertyPath
from gaphor.UML.uml import Dependency
class RelevantTo(Dependency, DirectedRelationshipPropertyPath):
    pass


class ControllingMeasure(Dependency, DirectedRelationshipPropertyPath):
    affects: relation_many[Property]


class Violates(Dependency):
    pass


class AnySituation(Situation):
    from_: relation_many[AnySituation]
    to: relation_many[AnySituation]


class AbstractEvent(AnySituation):
    pass


class AbstractCause(AbstractEvent):
    error: relation_many[DysfunctionalEvent]


class DysfunctionalEvent(AbstractEvent):
    error: relation_many[DysfunctionalEvent]
    failure: relation_many[DysfunctionalEvent]
    fault: relation_many[AbstractCause]
    fromError: relation_many[DysfunctionalEvent]
    toError: relation_many[DysfunctionalEvent]


class AbstractFailureMode(DysfunctionalEvent):
    pass


class AbstractEffect(DysfunctionalEvent):
    pass


class Effect(AbstractEffect):
    pass


class HarmPotential(AnySituation):
    pass


class Hazard(HarmPotential):
    pass


class Scenario(AnySituation):
    scenarioStep: relation_many[AnySituation]


class AbstractRisk(Scenario):
    harm: relation_many[AbstractEffect]
    harmPotential: relation_many[HarmPotential]
    trigger: relation_many[AbstractEvent]


from gaphor.UML.uml import Dependency
class Detection(ControllingMeasure, Dependency):
    pass


class Prevention(ControllingMeasure, Dependency):
    pass


class Mitigation(ControllingMeasure, Dependency):
    pass


class Recommendation(ControllingMeasure, Dependency):
    pass


from gaphor.UML.uml import State
class FailureState(State):
    pass


class FTAElement(DysfunctionalEvent):
    pass


class FTATree(FTAElement, Scenario):
    topEvent: relation_one[EventDef]


class Tree(Class):
    pass


class EventDef(FTAElement):
    pass


from gaphor.UML.uml import Event
class Gate(Class):
    pass


class DormantEvent(Class):
    pass


class BasicEvent(Class):
    pass


class ConditionalEvent(Class):
    pass


class ZeroEvent(Class):
    pass


class HouseEvent(Class):
    pass


class AND(Class):
    pass


class OR(Class):
    pass


class SEQ(Class):
    pass


class XOR(Class):
    pass


class INHIBIT(Class):
    pass


class MAJORITY_VOTE(Class):
    pass


class NOT(Class):
    pass


class IntermediateEvent(Class):
    pass


class TopEvent(Class):
    pass


from gaphor.UML.uml import Property
class TransferIn(Property):
    pass


class TransferOut(Class):
    pass


class BasicEventDef(EventDef):
    pass


class IntermediateEventDef(EventDef):
    pass


class TopEventDef(EventDef):
    pass


class ConditionalEventDef(EventDef):
    pass


class DormantEventDef(EventDef):
    pass


class UndevelopedEventDef(EventDef):
    pass


class HouseEventDef(EventDef):
    pass


class ZeroEventDef(EventDef):
    pass


from gaphor.core.modeling.element import Element
class Undeveloped(Element):
    pass


class GateDef():
    pass


class UndesiredState(DysfunctionalEvent):
    pass


class Cause(AbstractCause):
    pass


class MAJORITY_VOTE_Def(GateDef):
    pass


class NOT_Def(GateDef):
    pass


class OR_Def(GateDef):
    pass


class SEQ_Def(GateDef):
    pass


class XOR_Def(GateDef):
    pass


class AND_Def(GateDef):
    pass


class INHIBIT_Def(GateDef):
    condition: relation_many[EventDef]


class UnsafeControlAction_Def(Situation):
    Context: relation_one[AbstractOperationalSituation]
    harmPotential: relation_many[HarmPotential]


from gaphor.UML.uml import Property
class Actuator(Property):
    pass


from gaphor.UML.uml import DataType
class Signal():
    pass


class ControlAction(Class, DataType, Signal):
    pass


class ControlStructure(Block, Class):
    pass


class ControlledProcess(Property):
    pass


class Controller(Property):
    pass


class Feedback(Class, DataType, Signal):
    pass


class Sensor(Property):
    pass


class Early(UnsafeControlAction_Def):
    pass


class FailureMode():
    pass


class UnsafeControlAction(Class, FailureMode):
    pass


class OperationalSituation(Class):
    pass


class OperationalCondition(Situation):
    pass


class AbstractOperationalSituation(OperationalCondition):
    conditions: relation_many[OperationalCondition]


class Factor(AbstractCause):
    pass


class ProcessModel():
    pass


class InadequateControlExecution(ProcessModel):
    pass


class InadequateControllerDecisions(ProcessModel):
    pass


class InadequateFeedbackAndInputs(ProcessModel):
    pass


class InadequateProcessBehavior(ProcessModel):
    pass


class Late(UnsafeControlAction_Def):
    pass


class Loss(AbstractEffect):
    pass


class LossScenario(Scenario):
    Factor: relation_many[Factor]
    processModel: relation_many[ProcessModel]
    unsafeControlAction: relation_many[UnsafeControlAction_Def]


class NotProvided(UnsafeControlAction_Def):
    pass


class OutOfSequence(UnsafeControlAction_Def):
    pass


class Provided(UnsafeControlAction_Def):
    pass


class RiskRealization(AbstractRisk):
    pass


class Threat(Factor):
    pass



ControllingMeasure.affects = association("affects", Property, composite=True)
AnySituation.to = association("to", AnySituation, opposite="from_")
AnySituation.from_ = association("from_", AnySituation, opposite="to")
AbstractCause.error = association("error", DysfunctionalEvent, opposite="fault")
DysfunctionalEvent.fault = association("fault", AbstractCause, opposite="error")
DysfunctionalEvent.toError = association("toError", DysfunctionalEvent, opposite="fromError")
DysfunctionalEvent.fromError = association("fromError", DysfunctionalEvent, opposite="toError")
DysfunctionalEvent.error = association("error", DysfunctionalEvent, opposite="failure")
DysfunctionalEvent.failure = association("failure", DysfunctionalEvent, opposite="error")
Scenario.scenarioStep = association("scenarioStep", AnySituation, composite=True)
AbstractRisk.trigger = association("trigger", AbstractEvent, composite=True)
AbstractRisk.harmPotential = association("harmPotential", HarmPotential, composite=True)
AbstractRisk.harm = association("harm", AbstractEffect, composite=True)
FTATree.topEvent = association("topEvent", EventDef, upper=1, composite=True)
INHIBIT_Def.condition = association("condition", EventDef)
UnsafeControlAction_Def.Context = association("Context", AbstractOperationalSituation, upper=1)
UnsafeControlAction_Def.harmPotential = association("harmPotential", HarmPotential)
AbstractOperationalSituation.conditions = association("conditions", OperationalCondition, composite=True)
LossScenario.unsafeControlAction = association("unsafeControlAction", UnsafeControlAction_Def)
LossScenario.processModel = association("processModel", ProcessModel, composite=True)
LossScenario.Factor = association("Factor", Factor, composite=True)
