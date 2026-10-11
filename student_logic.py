def predict_performance(final_score):
    if final_score >= 75:
        return "High"
    elif final_score >= 50:
        return "Medium"
    else:
        return "Low"


if __name__ == "__main__":
    result = predict_performance(85)
    print("Predicted Performance Class:", result)
