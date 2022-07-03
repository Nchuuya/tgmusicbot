# 𝐌𝐨𝐝𝐮𝐥𝐞𝐬 𝐚𝐧𝐝 𝐄𝐧𝐯𝐢𝐫𝐨𝐧𝐦𝐞𝐧𝐭𝐬
import os
import aiohttp
from os import getenv
from dotenv import load_dotenv

# 𝐈𝐧𝐭𝐞𝐫𝐧𝐚𝐥 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 (@𝐀𝐝𝐢𝐭𝐲𝐚𝐇𝐚𝐥𝐝𝐞𝐫)
load_dotenv()
que = {}
admins = {}
aiohttpsession = aiohttp.ClientSession()

# 𝐑𝐞𝐪𝐮𝐢𝐫𝐞𝐝 𝐕𝐚𝐫𝐢𝐚𝐛𝐥𝐞𝐬 //𝐏𝐨𝐰𝐞𝐫𝐞𝐝 𝐁𝐲 @𝐀𝐝𝐢𝐭𝐲𝐚𝐇𝐚𝐥𝐝𝐞𝐫
API_HASH = getenv("API_HASH", "50c97a11b622575c5b9441b1062f601a")
API_ID = int(getenv("API_ID", "8714251"))
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "Assistant ♡")
ASSISTANT_USERNAME = getenv("ASSISTANT_USERNAME", "boa_assistant")
BOT_IMAGE = getenv("BOT_IMAGE", "https://telegra.ph/file/55a3552a9184f40a891c0.jpg")
BOT_NAME = getenv("BOT_NAME", "Boa Hancock")
BOT_TOKEN = getenv("BOT_TOKEN", "5276474965:AAFGJNgQEWJH1qQ8RlHBNAM9e3aJH7ke18c")
BOT_USERNAME = getenv("BOT_USERNAME", "boahancock_robot")
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "120"))
OWNER_NAME = getenv("OWNER_NAME", "Zhongli ♡")
OWNER_USERNAME = getenv("OWNER_USERNAME", "zerohisooka")
SOURCE_CODE = getenv("SOURCE_CODE", "https://t.me/trinetra_network")
STRING_SESSION = getenv("STRING_SESSION", "BQCjPGUQAotmHx2U6fA4EtOIitKQnbViiCAaIzlGX_u19OQRspGKp_JBP_kSVgihPThlOlFEiKllt4azR0HHdYav7GKMNAHIxI2U4MKAJoGWzYqPoUB5Nv4QL4rw1bhcLYBCNvbFmg4FgvpFgtEei0GIa9S8T5C3HJ3AJpMNtx9TL3Sth_zdI1snwqxUt3ad_ibQLT60gwBBRhmxadz8UKu8FBUu5SIg2fcMHjtW8MBltpQlM9hvpt8IPH4xfLv8vsnm7Iuk3LvaOMN92ZZ6XEdHLmYMooiemVAbhgeSN0Wk9vpUP5ydf12QXh-KFR1aG08fAVFN1uNWYUhRwvikY1SMAAAAAHsrA8MA")
SUDO_USERS = list(map(int, getenv("SUDO_USERS", "2066416579").split()))
SUPPORT_GROUP = getenv("SUPPORT_GROUP", "https://t.me/ahjin_networkk")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "https://t.me/boa_updates")

# 𝐃𝐨 𝐍𝐨𝐭 𝐂𝐡𝐚𝐧𝐠𝐞 𝐓𝐡𝐢𝐬 𝐋𝐢𝐧𝐞𝐬 // 𝐈𝐠𝐧𝐨𝐫𝐞 𝐓𝐡𝐢𝐬 (Brutal Rajput) 
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
PROFILE_CHANNEL = getenv("PROFILE_CHANNEL", "https://t.me/ahjin_networkk")
