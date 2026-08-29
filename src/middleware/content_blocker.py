from langchain.agents.middleware import AgentMiddleware, AgentState, hook_config
from langchain.messages import HumanMessage, AIMessage
from langgraph.runtime import Runtime
from typing import Any

class WordBlockMiddleWare(AgentMiddleware):
    def __init__(self, blocked_terms:list[str]):
        super().__init__()
        self.blocked_terms = [term.lower() for term in blocked_terms]


    def _get_last_message(self, state: AgentState):
        for msg in reversed(state['messages']):
            if isinstance(msg, HumanMessage):
                return msg.content


    @hook_config(can_jump_to=['end'])
    def before_model(self, state: AgentState, runtime: Runtime) -> dict[str, Any] | None:
        message = self._get_last_message(state)
        processed_text = message.lower()

        block = False
        for term in self.blocked_terms:
            if term in processed_text:
                block = True
                break

        if block:
            return {
                "messages" : [AIMessage("I am sorry, but your request breaks the guardrails placed on me!")],
                'jump_to':'end'
            }

        return None



