import requests
from bs4 import BeautifulSoup
from fastapi import APIRouter
from typing import Dict

router: APIRouter = APIRouter()

headers: dict = {
    "content-type": "text/html; charset=UTF-8",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:87.0) Gecko/20100101 Firefox/87.0"
}


@router.get("/")
async def index() -> str:
    return "MCBBS USER API"


@router.get("/stats/{uid}")
async def stats(uid: int) -> Dict[str, str]:
    result: Dict[str, str] = {}
    res: requests.Response = requests.get(
        "https://www.mcbbs.net/home.php?uid={uid}".format(uid=uid),
        headers=headers
    )
    soup: BeautifulSoup = BeautifulSoup(res.text, "html5lib")
    for i, v in enumerate(soup.find_all("li")[-10: -1]):
        v_soup: BeautifulSoup = BeautifulSoup(str(v), "html5lib")
        result[v_soup.find("em").text] = v_soup.find("li").contents[1].text
    return result
