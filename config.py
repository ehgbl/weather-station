from dotenv import load_dotenv
import os

load_dotenv()
openweatherAPI=os.getenv("OPENWEATHER_API_KEY")
print(openweatherAPI)
