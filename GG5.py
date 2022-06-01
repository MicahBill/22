from linepy import *
from akad.ttypes import *
from akad.ttypes import Message
from akad.ttypes import ContentType as Type
from akad.ttypes import TalkException
from akad.ttypes import IdentityProvider, LoginResultType, LoginRequest, LoginType
from akad.ttypes import LiffChatContext, LiffContext, LiffSquareChatContext, LiffNoneContext, LiffViewRequest
from akad.ttypes import ChatRoomAnnouncementContents
from akad.ttypes import Location
from akad.ttypes import ChatRoomAnnouncement
import LINETCR
from LINETCR.lib.curve.ttypes import *
from thrift import transport, protocol, server
from thrift.Thrift import *
from thrift.unverting import *
from thrift.TMultiplexedProcessor import *
from thrift.TSerialization import *
from thrift.TRecursive import *
from thrift import transport, protocol, server
from thrift.protocol import TCompactProtocol, TMultiplexedProtocol, TProtocol
from thrift.transport import TTransport, TSocket, THttpClient, TZlibTransport
from multiprocessing import Pool, Process
from time import sleep
import pytz, datetime, time, timeit, livejson,asyncio, random, sys, ast, re, os, json, subprocess, threading, string, codecs, requests, ctypes, urllib, traceback, tempfile, platform
from humanfriendly import format_timespan, format_size, format_number, format_length
from datetime import timedelta, date
from datetime import datetime
from threading import Thread, activeCount


_session = requests.session()
try:
    import urllib.request as urllib2
except ImportError:
    import urllib2

programStart = time.time()

b1 = LINECR.LINE
b1.login(token="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJqdGkiOiI3ZDEwZTdjOC1mNzNmLTRiZjctOTI1OC1hNWYzMjA1OGJlMjUiLCJhdWQiOiJMSU5FIiwiaWF0IjoxNjUzNTkyNDkxLCJleHAiOjE2NTQxOTcyOTEsInNjcCI6IkxJTkVfQ09SRSIsInJ0aWQiOiIyMWUxMjBmNy1mMDYzLTRmZGMtOWIwMi04YjQyMDE2OTQ1NTQiLCJyZXhwIjoxODExMjcyNDkxLCJ2ZXIiOiIzLjEiLCJhaWQiOiJ1N2FjNzhiOGY0ZDY2MDY5ZTljYTI0MTA1ZGM5MDM5N2UiLCJsc2lkIjoiOTZmN2M2YzktZDRmNy00MmY2LTk2ZjUtYjA5YjA0OTlmM2NlIiwiZGlkIjoiZTFjN2EwYzlmZWE0NmQwZDU2ZjM3YTI0ZDNlN2M4ZGEiLCJjdHlwZSI6IkFORFJPSUQiLCJjbW9kZSI6IlBSSU1BUlkiLCJjaWQiOiIwMDAwMDAwMDAwIn0.8heh18PTdKmv2bGu-UW5NYg8-BYgomjlZwXMlWckW_8")
b1.loginResult()
print('logged in..')

print('Done, working!!')

owner=["u0be40d5b6854cce0f78b76a7ace30727"]


elif "Bc " in msg.text:
    if msg.from_ in owner:
        bctxt = msg.text.replace("Bc ","")
        a = b1.getGroupIdsJoined()for taf in a:
        b1.sendText(taf, (bctxt))
