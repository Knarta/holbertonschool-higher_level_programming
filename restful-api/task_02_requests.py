#!/usr/bin/python3

"""Task 2: Fetch posts from the API and save them to a CSV file"""

import requests
import csv

"""Fetch posts from the API"""

response = requests.get('https://jsonplaceholder.typicode.com/posts')
statuscode = response.status_code

"""Function to fetch and print posts"""


def fetch_and_print_posts():
    print(f"Status Code: {statuscode}")
    if statuscode == 200:
        for post in response.json():
            print(post["title"])


"""Function to fetch and save posts to a CSV file"""


def fetch_and_save_posts():
    if statuscode == 200:
        posts = response.json()
        with open("posts.csv", mode="w", newline='') as file:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for post in posts:
                filtered_post = {key: post[key] for key in fieldnames}
                writer.writerow(filtered_post)


if __name__ == '__main__':
    fetch_and_print_posts()
    fetch_and_save_posts()
