# llm_interface.py

def get_sql_query(nl_question):
    q = nl_question.lower()

    if "total sales" in q:
        return "SELECT SUM(total_sales) FROM total_sales;"

    elif "roas" in q or "return on ad spend" in q:
        return """
        SELECT SUM(t.total_sales) / SUM(a.ad_spend)
        FROM ad_sales a
        JOIN total_sales t ON a.product_id = t.product_id;
        """

    elif "highest cpc" in q:
        return "SELECT product_id, cpc FROM ad_sales ORDER BY cpc DESC LIMIT 1;"

    elif "eligible products" in q:
        return "SELECT * FROM eligibility WHERE is_eligible = 1;"

    else:
        return "-- I couldn't understand your question."

def format_answer(question, sql, result):
    return {
        "question": question,
        "generated_sql": sql,
        "result": result
    }
