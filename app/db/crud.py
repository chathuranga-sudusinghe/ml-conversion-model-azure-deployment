from .connection import get_connection


def insert_raw_input(data: dict):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO ml.raw_inputs (
        customer_id, age, gender, income, campaign_channel,
        campaign_type, ad_spend, click_through_rate,
        website_visits, pages_per_visit, time_on_site,
        social_shares, email_opens, email_clicks,
        previous_purchases, loyalty_points,
        advertising_platform, advertising_tool
    )
    VALUES (
        %(CustomerID)s, %(Age)s, %(Gender)s, %(Income)s, %(CampaignChannel)s,
        %(CampaignType)s, %(AdSpend)s, %(ClickThroughRate)s,
        %(WebsiteVisits)s, %(PagesPerVisit)s, %(TimeOnSite)s,
        %(SocialShares)s, %(EmailOpens)s, %(EmailClicks)s,
        %(PreviousPurchases)s, %(LoyaltyPoints)s,
        %(AdvertisingPlatform)s, %(AdvertisingTool)s
    )
  """


    cursor.execute(query, data)
    conn.commit()
    cursor.close()
    conn.close()


def insert_prediction(customer_id: int, probability: float, prediction: int):
    conn = get_connection()
    cursor = conn.cursor()

    query = """
    INSERT INTO ml.predictions (
        customer_id, probability, predicted_label, model_version
    )
    VALUES (%s, %s, %s, %s)
    """

    cursor.execute(query, (int(customer_id),float(probability),int(prediction),"v2"))
    conn.commit()
    cursor.close()
    conn.close()

