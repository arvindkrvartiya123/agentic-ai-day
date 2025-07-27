import os
from google.adk.agents import Agent
# from google.adk.tools import google_search
from google.genai import types

from agribotics.prompt import ROOT_AGENT_INSTRUCTION, GOVERNMENT_SCHEME_INSTRUCTION, CROP_AND_SOIL_ANALYST_INSTRUCTION
from agribotics.tools import get_weather, search_google_serper, buy_crop, sale_crop, buy_fertilizer
api_key=os.getenv('SERPER_KEY')

government_scheme_agent = Agent(
    name="government_scheme_agent",
    model="gemini-live-2.5-flash-preview-native-audio",
    description="This agent will give info about government scheme in Agriculture sector.",
    instruction=GOVERNMENT_SCHEME_INSTRUCTION,
    tools=[search_google_serper],
)

crop_and_soil_analyst_agent = Agent(
    name="crop_and_soil_analyst_agent",
    model="gemini-live-2.5-flash-preview-native-audio",
    description="This bot will take crop or soil info or image and give analysis",
    instruction=CROP_AND_SOIL_ANALYST_INSTRUCTION,
    tools=[search_google_serper],
)

crop_price_prediction_agent = Agent(
    name="crop_price_prediction",
    model="gemini-live-2.5-flash-preview-native-audio",
    description="This bot will give future price of crop based  on satalite image, historical data, and weather info",
    instruction=CROP_AND_SOIL_ANALYST_INSTRUCTION,
    tools=[get_weather, search_google_serper],
)


root_agent = Agent(
    name="adk_short_bot",
    model="gemini-live-2.5-flash-preview-native-audio", #gemini-live-2.5-flash-preview-native-audio, gemini-live-2.5-flash, gemini-2.5-flash
    description="this is main agent this will transfer user query to respective agent",
    instruction=ROOT_AGENT_INSTRUCTION,
    tools=[buy_crop, sale_crop, buy_fertilizer],
    sub_agents=[government_scheme_agent, crop_and_soil_analyst_agent, crop_price_prediction_agent]
)
