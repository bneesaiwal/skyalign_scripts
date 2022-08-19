#!/usr/bin/python Python

"""
This script takes fasta alignment files and creates hmm consensus logos using the skylign api

@Author Aneel Biswas
@Version 1.0
@Date 2022Aug18
"""

from __future__ import annotations

import asyncio
from asyncio import gather, sleep, run
import os
import json

import requests


INPUT_DIR = '/Users/aneelbiswas/PycharmProjects/skyalign_scripts/skyalign_scripts/test_supplemental/test_infiles'
OUTPUT_DIR = '/Users/aneelbiswas/PycharmProjects/skyalign_scripts/skyalign_scripts/test_supplemental/test_outfiles'
BATCH_SIZE = 50


async def skylign_post(skylign_url: str, header_dict: dict[str: str],
                       file_dict: dict[str: str], response_dict: dict[str: str]) -> None:

    response_dict[file_dict['file'][0]] = requests.post(skylign_url, headers=header_dict, files=file_dict)

    return None


async def create_response_dict(batch_size, fasta_list) -> dict[str: requests.Response]:
    skylign_url = 'http://skylign.org/'
    response_dict = {}
    batch_number = len(fasta_list) // BATCH_SIZE

    for batch in range(batch_number):
        tasks = []
        for i in range(batch_size):
            fasta = fasta_list[batch * batch_size + i]
            tasks.append(asyncio.create_task(skylign_post(
                skylign_url, {'Accept': 'application/json'},
                {'file': (f'{INPUT_DIR}/{fasta}', open(f'{INPUT_DIR}/{fasta}', 'rb'))}, response_dict)))
        await gather(*tasks, sleep(1))
    # If last batch is not batch size finishes remainder of list
    tasks = []
    for i in range(batch_size * batch_number, len(fasta_list)):
        fasta = fasta_list[i]
        tasks.append(asyncio.create_task(skylign_post(
            skylign_url, {'Accept': 'application/json'},
            {'file': (f'{INPUT_DIR}/{fasta}', open(f'{INPUT_DIR}/{fasta}', 'rb'))}, response_dict)))
    await gather(*tasks, sleep(1))

    return response_dict


async def skylign_get(get_url: str, fasta: str, json_responses_dict: dict) -> None:
    get_url = get_url[:4] + get_url[5:]
    json_responses_dict[fasta] = requests.get(get_url, headers={'Accept': 'application/json'})
    return None


async def save_consensus_logos(response_dict: dict[str: requests.Response], output_dir: str) -> None:
    json_responses_dict = {}
    tasks = []
    for fasta, response in response_dict.items():
        print(response.json())
        tasks.append(
            asyncio.create_task(
                skylign_get(response.json()['url'], fasta, json_responses_dict)))
    await gather(*tasks)
    for fasta, logo in json_responses_dict.items():
        print(fasta)
        with open(f'{output_dir}/{fasta.split(sep="/")[-1][:-6]}_logo.json', 'w', encoding='utf8') as json_file:
            json.dump(logo.json(), json_file)
    return None


async def main() -> None:
    fasta_list = os.listdir(INPUT_DIR)
    response_dict = await create_response_dict(BATCH_SIZE, fasta_list)
    await save_consensus_logos(response_dict, OUTPUT_DIR)
    return None


if __name__ == "__main__":
    run(main())
