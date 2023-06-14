import requests


class Nutritionix:
    # https://docs.google.com/document/d/1_q-K-ObMTZvO0qUEAxROrN3bwMujwAN25sLHwJzliK0/edit#bookmark=id.auzu6vhyq4ei
    def __init__(self, app_id, api_key):
        self.app_id = app_id
        self.api_key = api_key
        self.api_endpoint = 'https://trackapi.nutritionix.com/v2/natural/nutrients'

    def get_calories(self, food_name):
        headers = {
            'Content-Type': 'application/json',
            'x-app-id': self.app_id,
            'x-app-key': self.api_key
        }

        data = {
            'query': food_name,
            'timezone': 'Asia/Kolkata'
        }

        try:
            response = requests.post(self.api_endpoint, json=data, headers=headers)
            response.raise_for_status()
            data = response.json()

            if 'foods' in data:
                first_food = data['foods'][0]
                food_name = first_food['food_name']
                calories = first_food['nf_calories']
                return food_name, calories
            else:
                return None

        except requests.exceptions.HTTPError as err:
            print(f"HTTP Error: {err}")
        except requests.exceptions.RequestException as err:
            print(f"Request Exception: {err}")


if __name__ == '__main__':
    app_id = "ID Here"
    api_key = "Key Here"

    food_name = "Food Name Here"
    nutritionix = Nutritionix(app_id, api_key)
    result = nutritionix.get_calories(food_name)

    if result:
        food_name, calories = result
        print(f"Calories in {food_name}: {calories}")
    else:
        print("Food not found or error occurred.")
