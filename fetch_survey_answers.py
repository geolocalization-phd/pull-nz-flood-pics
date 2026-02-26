import requests
import json
import time

SURVEY_ID = "8"


def fetch_all_pages(url, params, csv=False):
    answers_fetched = -1
    while True:
        print(params)
        response = requests.get(url, params)
        if csv:
            response_text = response.text
        else:
            response_text = response.json()
        print(len(response_text))
        if len(response_text) == 0:
            break
        yield response_text
        time.sleep(10)
        params["page_number"] += 1


def get_survey_answers_csv(survey_id):
    url = f"https://citizenscience-api.niwa.co.nz/api/surveys/{survey_id}/answers.csv"
    params = {
        "page_number": 1,
        "limit": 1000,
        "with_values": True,
        "bbox": "[118.513,-46.608,218.493,-32.251,4326]",
    }
    for paged_data in fetch_all_pages(url, params, csv=True):
        with open(
            f"fetched_answers_survey_{survey_id}_{params['page_number']}.csv", "w"
        ) as f:
            f.write(paged_data)


# know that there are up to 9000 answers
def get_survey_answers_json(survey_id):
    url = f"https://citizenscience-api.niwa.co.nz/api/surveys/{survey_id}/answers"
    params = {
        "page_number": 1,
        "limit": 1000,
        "with_values": True,
        "bbox": "[118.513,-46.608,218.493,-32.251,4326]",
    }

    for paged_data in fetch_all_pages(url, params):
        # data_entry = item.json()
        with open(
            f"fetched_answers_survey_{survey_id}_{params['page_number']}.json", "w"
        ) as f:
            json.dump(paged_data, f)


if __name__ == "__main__":
    answers = get_survey_answers_csv(SURVEY_ID)
