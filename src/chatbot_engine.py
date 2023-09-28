from langchain.chat_models import AzureChatOpenAI
import langchain
from langchain.memory import ChatMessageHistory
from langchain.schema import HumanMessage

langchain.verbose = True


def chat(message: str, history: ChatMessageHistory) -> str:
  llm = AzureChatOpenAI(
    client=None,
    deployment_name="gpt-35-turbo",
    temperature=0,
    request_timeout=180,
  )
  messages = history.messages
  # messages.append(HumanMessage(content=message))
  print(messages)
  return llm(messages).content