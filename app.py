import streamlit as st

from breaking_bad.lib import get_quote

response = get_quote()  # assuming the function returns an author and a quote

f"{response}"

