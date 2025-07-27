from google.adk.agents import Agent

from agribotics_agent.prompt import ROOT_AGENT_INSTRUCTION
# from agribotics_agent.tools.live_agent import connect_video_call

root_agent = Agent(
    name="agribotics_agent",
    model="gemini-2.0-flash",
    description="A bot that can connect users on a video call.",
    instruction=ROOT_AGENT_INSTRUCTION
)
#tools=[connect_video_call],