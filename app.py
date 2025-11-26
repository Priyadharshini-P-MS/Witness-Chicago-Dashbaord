import streamlit as st
import pandas as pd
import altair as alt

# Load the updated dataset
df = pd.read_csv("corpus_updated.csv")

# Title and subtitle
st.title("📊 Witness Archive Dashboard")
st.subheader("Public Sentiment and Events Related to ICE in Chicago")

# Basic stats
st.markdown("### Summary")
st.write("Total records (filtered)", len(df))
st.write("Unique articles", df['article_id'].nunique())
st.write("Date range", f"{df['date_published'].min()} → {df['date_published'].max()}")

# Emotion distribution
st.markdown("### Emotion distribution")
emotion_chart = (
    alt.Chart(df)
    .mark_bar()
    .encode(
        x=alt.X("emotion", sort='-y'),
        y="count()",
        tooltip=["emotion", "count()"]
    )
    .properties(width=700)
)
st.altair_chart(emotion_chart, use_container_width=True)

# Article sources
st.markdown("### Sources (top 10)")
st.write(df['source'].value_counts().head(10))

# Optional filters or raw data display
with st.expander("Show raw data"):
    st.dataframe(df)