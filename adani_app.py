{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": 1,
   "id": "b4c8eba3-d4e6-4fdf-b8b5-4e7da93adf57",
   "metadata": {},
   "outputs": [
    {
     "name": "stderr",
     "output_type": "stream",
     "text": [
      "2025-06-28 13:50:14.748 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:14.750 WARNING streamlit.runtime.scriptrunner_utils.script_run_context: Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:15.563 \n",
      "  \u001b[33m\u001b[1mWarning:\u001b[0m to view this Streamlit app on a browser, run it with the following\n",
      "  command:\n",
      "\n",
      "    streamlit run C:\\Users\\swamy\\AppData\\Local\\Programs\\Orange\\Lib\\site-packages\\ipykernel_launcher.py [ARGUMENTS]\n",
      "2025-06-28 13:50:15.563 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:15.564 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:15.605 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:15.606 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:15.606 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:15.608 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:15.611 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:15.613 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:15.615 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:15.617 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:15.618 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:15.622 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:15.624 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:15.627 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:16.128 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:16.128 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:16.130 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:16.131 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:16.132 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:16.134 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:16.136 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:16.137 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:16.255 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:16.256 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:16.257 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:16.258 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n",
      "2025-06-28 13:50:16.259 Thread 'MainThread': missing ScriptRunContext! This warning can be ignored when running in bare mode.\n"
     ]
    },
    {
     "data": {
      "text/plain": [
       "DeltaGenerator()"
      ]
     },
     "execution_count": 1,
     "metadata": {},
     "output_type": "execute_result"
    }
   ],
   "source": [
    "import streamlit as st\n",
    "import pandas as pd\n",
    "import plotly.express as px\n",
    "\n",
    "st.set_page_config(layout=\"wide\")\n",
    "st.title(\"📈 Adani Enterprises Stock Market Analysis\")\n",
    "\n",
    "# Load the dataset\n",
    "df = pd.read_csv(r\"C:\\Users\\swamy\\Desktop\\Zidio Internship\\Quote-Equity-ADANIENT-EQ-27-06-2024-to-27-06-2025.csv\")\n",
    "\n",
    "# Clean column names\n",
    "df.columns = df.columns.str.strip()\n",
    "\n",
    "# Convert Date column to datetime and sort\n",
    "df['Date'] = pd.to_datetime(df['Date'], format='%d-%b-%y')\n",
    "df = df.sort_values(by='Date')\n",
    "\n",
    "# Sidebar options\n",
    "st.sidebar.header(\"Options\")\n",
    "show_data = st.sidebar.checkbox(\"Show Raw Data\")\n",
    "\n",
    "if show_data:\n",
    "    st.subheader(\"Raw Data\")\n",
    "    st.write(df)\n",
    "\n",
    "st.subheader(\"📉 Closing Price Over Time\")\n",
    "fig = px.line(df, x='Date', y='close', title='Adani Closing Prices')\n",
    "st.plotly_chart(fig, use_container_width=True)\n",
    "\n",
    "st.subheader(\"📊 Volume Traded Over Time\")\n",
    "fig2 = px.bar(df, x='Date', y='Volume', title='Trading Volume')\n",
    "st.plotly_chart(fig2, use_container_width=True)\n",
    "\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": 3,
   "id": "1d26d27d-27f6-4eb8-8fe5-407b12d8d9e2",
   "metadata": {},
   "outputs": [
    {
     "ename": "SyntaxError",
     "evalue": "invalid syntax (1652497480.py, line 1)",
     "output_type": "error",
     "traceback": [
      "\u001b[1;36m  Cell \u001b[1;32mIn[3], line 1\u001b[1;36m\u001b[0m\n\u001b[1;33m    streamlit run adani_app.py\u001b[0m\n\u001b[1;37m              ^\u001b[0m\n\u001b[1;31mSyntaxError\u001b[0m\u001b[1;31m:\u001b[0m invalid syntax\n"
     ]
    }
   ],
   "source": [
    "streamlit run adani_app.py\n"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "9b3c21ec-67ae-46bd-9b64-e30ceb6c013a",
   "metadata": {},
   "outputs": [],
   "source": []
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": "Python [conda env:Orange]",
   "language": "python",
   "name": "conda-env-Orange-py"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.11.8"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
