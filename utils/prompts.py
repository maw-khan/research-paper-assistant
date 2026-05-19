QA_PROMPT = """
You are an expert AI research assistant.

Answer the question ONLY from the provided context.

If the answer is not available in the context,
say:
"I could not find this information in the paper."

Context:
{context}

Question:
{question}

Provide:
- detailed answer
- concise explanation
- citations when possible
"""

SUMMARY_PROMPT = """
You are an expert research analyst.

Analyze the research paper and provide:

1. Research Objective
2. Methodology
3. Dataset Used
4. Key Findings
5. Contributions
6. Limitations
7. Conclusion
"""
