import os

from dotenv import load_dotenv
from fastapi import FastAPI
import streamlit as st

load_dotenv()

app = FastAPI(title="Smart Loadshedding Advisor")


@app.get("/health")
def health_check() -> dict:
    return {"status": "ok", "service": "smart-loadshedding-advisor"}


def run_streamlit() -> None:
    st.set_page_config(page_title="Smart Loadshedding Advisor")
    st.title("Smart Loadshedding Advisor")
    st.write("Placeholder UI for the Streamlit frontend.")
    st.caption("API health endpoint available at /health")


if __name__ == "__main__":
    run_streamlit()
