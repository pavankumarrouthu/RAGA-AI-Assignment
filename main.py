from fastapi import FastAPI
from data_ingestion.api_agent import APIAgent
from data_ingestion.scraping_agent import ScrapingAgent
from agents.retriever import RetrieverAgent
from agents.analyzer import AnalyzerAgent
from agents.language_agent import LanguageAgent

app = FastAPI()

api_agent = APIAgent(api_key='YOUR_API_KEY')
scraping_agent = ScrapingAgent()
retriever_agent = RetrieverAgent()
analyzer_agent = AnalyzerAgent()
language_agent = LanguageAgent()

@app.get("/market-brief")
async def get_market_brief(symbol: str):
    market_data = api_agent.fetch_market_data(symbol)
    filings = scraping_agent.scrape_filings("https://example.com/filings")
    # Process data
    risk_exposure = analyzer_agent.analyze_data(market_data)
    narrative = language_agent.generate_narrative(market_data)
    return {"risk_exposure": risk_exposure, "narrative": narrative}
