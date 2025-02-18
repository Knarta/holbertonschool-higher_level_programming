#!/usr/bin/python3

import requests
import csv

response = requests.get("https://jsonplaceholder.typicode.com/posts")
status_code = response.status_code


def fetch_and_print_posts():
    print(f"Status code: {status_code}")
    if response.status_code == 200:
        for post in response.json():
            print(post['title'])


def fetch_and_save_posts():
    if response.status_code == 200:
        posts = response.json()
        with open("posts.csv", "w") as file:
            fieldnames = ['id', 'title', 'body']
            writer = csv.DictWriter(file, fieldnames=fieldnames)
            writer.writeheader()
            for post in posts:
                fieltered_post = {key: post[key] for key in fieldnames}
                writer.writerow(fieltered_post)
