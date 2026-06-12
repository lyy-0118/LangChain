from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, SystemMessage
from langchain_core.output_parsers import StrOutputParser

# 1.定义⼤模型
model = ChatOpenAI(
    model="deepseek-chat"
)
# 2.定义消息列表
messages = [
    SystemMessage(content="Translate the following from English into Chinese"),
    HumanMessage(content="hi!"),
]
# 3.定义输出解析器组件
parser = StrOutputParser()
# 4.定义链  调用大模型组件和解析器组件
chain = model | parser
# 5.执⾏链
print(chain.invoke(messages))