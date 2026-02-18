import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

try:
    connection = psycopg2.connect(
        host=os.getenv("DB_HOST"),
        database=os.getenv("DB_NAME"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        port=os.getenv("DB_PORT"),
        sslmode="require"
    )

    cursor = connection.cursor()

    # Simulated user input
    user_input = {
        "customer_id": 900003,
        "age": 35,
        "gender": "Male",
        "income": 70000,
        "campaign_channel": "Email",
        "campaign_type": "Seasonal",
        "ad_spend": 2000.0,
        "click_through_rate": 0.18,
        "conversion_rate": 0.07,
        "website_visits": 25,
        "pages_per_visit": 4.5,
        "time_on_site": 210.0,
        "social_shares": 15,
        "email_opens": 8,
        "email_clicks": 5,
        "previous_purchases": 4,
        "loyalty_points": 250,
        "advertising_platform": "Google",
        "advertising_tool": "AdsManager"
    }

    # Insert raw input
    insert_raw_query = """
    INSERT INTO ml.raw_inputs (
        customer_id, age, gender, income,
        campaign_channel, campaign_type, ad_spend,
        click_through_rate, conversion_rate,
        website_visits, pages_per_visit, time_on_site,
        social_shares, email_opens, email_clicks,
        previous_purchases, loyalty_points,
        advertising_platform, advertising_tool
    )
    VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);
    """

    cursor.execute(insert_raw_query, tuple(user_input.values()))

    # 🔥 Simulated model prediction
    probability = 0.78
    predicted_label = 1
    model_version = "v1"

    # Insert prediction
    insert_prediction_query = """
    INSERT INTO ml.predictions (
        customer_id, probability, predicted_label, model_version
    )
    VALUES (%s, %s, %s, %s);
    """

    cursor.execute(
        insert_prediction_query,
        (user_input["customer_id"], probability, predicted_label, model_version)
    )

    connection.commit()

    print("✅ Raw input and prediction inserted successfully!")

    cursor.close()
    connection.close()

except Exception as e:
    print("❌ Error:", e)
