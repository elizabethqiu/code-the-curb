import requests     # get_data, post_data
import api_requests, data_processing  # load_data, process_data

# EXAMPLE_GET_URL = "https://jsonplaceholder.typicode.com/todos/1"
GET_URL = "https://candidate.hubteam.com/candidateTest/v3/problem/dataset?userKey=0c59bc91319c73960149a72b848f"
POST_URL = "https://candidate.hubteam.com/candidateTest/v3/problem/result?userKey=0c59bc91319c73960149a72b848f"

# TEST_DATA_GET_URL = "https://candidate.hubteam.com/candidateTest/v3/problem/test-dataset?userKey=0c59bc91319c73960149a72b848f"
# TEST_SOLN_GET_URL = "https://candidate.hubteam.com/candidateTest/v3/problem/test-dataset-answer?userKey=0c59bc91319c73960149a72b848f"
# TEST_POST_URL = "https://candidate.hubteam.com/candidateTest/v3/problem/test-result?userKey=0c59bc91319c73960149a72b848f"


def main():
    api_requests.get_parking_status()

    processed_data = data_processing.process_data(data)
    print(f"processed data is here!\n{processed_data}")
    data3 = {'results': processed_data}
    print('CHECK', data2, data3)

    print('matches = ', data3 == data2)

    # response = api_requests.post_data(POST_URL, data3)
    # print(f"data posted successfully! response = {response}")


if __name__ == "__main__":
    main()