import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go
from collections import defaultdict

# Set page config for a more appealing look
st.set_page_config(layout="wide", page_title="Aslan Hattukai", page_icon="📊")

# Custom CSS for color scheme
st.markdown("""
<style>
    :root {
        --primary-color: #007FFF; /* Azure color */
        --secondary-color: #ffffff;
        --text-color: #000000;
        --background-color: #ffffff;
    }
    body, .stApp {
        color: var(--text-color);
        background-color: var(--background-color);
    }
    .stButton>button {
        color: var(--secondary-color);
        background-color: var(--primary-color);
        border-color: var(--primary-color);
    }
    .stSelectbox, .stTab {
        color: var(--text-color);
    }
    h1, h2, h3, h4, h5, h6, a {
        color: var(--primary-color);
    }
    .stTextInput > div > div > input {
        color: var(--text-color);
        background-color: var(--background-color);
    }
    .css-1cpxqw2, .css-2trqyj, .css-1d391kg {
        flex-direction: column;
    }
    .css-1cpxqw2 img {
        max-width: 100%;
        height: auto;
    }
</style>
""", unsafe_allow_html=True)

# Title and contact information
col1, col2 = st.columns([3, 1])

with col1:
    st.title("Aslan Hattukai")
    st.header("Data Engineer")

with col2:
    st.image("image.jpg", width=150)  # Replace with your image URL
# Intro
st.header("Introduction")
st.markdown("""
Data Specialist focused on driving threat intelligence through high-quality data.
Expertise includes developing analytical frameworks, leveraging cloud stacks (AWS, Snowflake, dbt), 
and implementing stringent validation and monitoring protocols crucial for training and validating AI/ML models.
Dedicated to data reliability and serving as the key analysis focal point for research and product teams.
""")

# Skills Section
st.header("Skills")

# Create two columns
col1, col2 = st.columns([3, 2])

with col1:
    # Radar chart code (unchanged)
    technology_stack = {
        "Cloud Platforms": ["Microsoft Azure", "AWS", "Snowflake"],
        "Data Engineering": ["dbt", "Databricks", "Apache Spark", "SSIS/SSMS"],
        "Frameworks": ["Kedro", "Django", "Streamlit", "FastAPI", "SQL Alchemy"],
        "Visualization": ["PowerBI"],
        "DevOps": ["Airflow", "ArgoCD/Jenkins", "Docker/Kubernetes"],
        "Development Tools": ["Jupyter notebook", "Bitbucket/Github", "Jira", "VSCode"],
        "Specialized Tools": ["BIOVIA Compose", "CISPRO", "ELN"]
    }
    expertise = {
        "Cloud Platforms": 7,
        "Data Engineering": 9,
        "Frameworks": 8,
        "Visualization": 8,
        "DevOps": 8,
        "Development Tools": 8,
        "Specialized Tools": 7
    }
    categories = list(expertise.keys())
    values = list(expertise.values())

    fig = go.Figure()
    fig.add_trace(go.Scatterpolar(
        r=values + values[:1],
        theta=categories + categories[:1],
        fill='toself',
        name='Skills',
        hoverinfo='text',
        text=[f"{cat}: {val}{', '.join(technology_stack[cat])}" for cat, val in zip(categories, values)],
        line=dict(color='#3498db')
    ))

    fig.update_layout(
        polar=dict(
            radialaxis=dict(
                visible=True,
                range=[0, 10]
            ),
            bgcolor='rgba(240, 242, 246, 0.8)'
        ),
        showlegend=False,
        paper_bgcolor='rgba(0,0,0,0)',
        plot_bgcolor='rgba(0,0,0,0)',
        height=500  # Adjust this value to control the height of the chart
    )
    st.plotly_chart(fig, use_container_width=True)

with col2:
    # Add some vertical space before the text
    st.write("")
    st.write("")
    st.write("")
    
    # Technology stack text
    st.markdown("""
    **Data Engineering:** dbt, Databricks, Apache Spark, SSIS/SSMS

    **Frameworks:** Kedro, Django, Streamlit, FastAPI, SQL Alchemy

    **Visualization:** PowerBI, Tableau

    **DevOps:** Airflow, ArgoCD, Jenkins, Docker, Kubernetes

    **Development Tools:** Jupyter notebook, Bitbucket/Github, Jira, VSCode

    **Specialized Tools:** BIOVIA Compose, CISPRO, ELN
    """)

# Experience Section
st.header("Experience")

experience = [
    {
        "role": "Data Engineer",
        "company": "J&J/Clinical IT",
        "dates": "08 2024 – Present",
        "description": """
        The Clinical IT Data Team supports Johnson & Johnson’s medical research initiatives by ingesting, processing, and delivering high-quality reseach data. The team recently transitioned to a modern cloud-based stack using AWS and Snowflake, with Datacoves (dbt, Airflow) and Permafrost enabling agile data pipeline development.
        - Designed and implemented robust ingestion frameworks tailored to diverse source systems, with built-in monitoring.
        - Work closely business stakeholders to gather requirements and translate them into scalable data infrastructure solutions.
        - Developed and orchestrated data pipelines and transformation workflows using Apache Airflow and dbt.
        - Built dashboards and operational monitoring tools to track data quality, pipeline performance, and business KPIs.
        - Implemented automated alerting and notification systems for pipeline failures using Jenkins, Bitbucket.

        """
    },
    {
        "role": "Application Developer",
        "company": "Arvesta/ Fertilizer tool",
        "dates": "04 2024 – ongoing",
        "description": """
        Arvesta is a prominent agricultural and horticultural company. They have been aiming to develop a module to aid them in recommending tailored fertilization considering government limits, long term soil health and environmental impact. To make full use and test the model that their R&D team has built we translate the models into an application that can be used by their farm advisors in the field.
        - Set up project plan, implementation and testing and deployment approach.
        - Work closely with the R&D team to translate the module rules to a Streamlit based multipage app.
        - Build a data model to store the generated and required data for the application.
        - Design a user friendly app workflow together with the end users.
        """
    },
    {
        "role": "Data Engineer",
        "company": "Mobile Vikings/ Byta",
        "dates": "05 2024 – 07 2024",
        "description": """
        Mobile Vikings is a telecommunications company that is part of Proximus. Until recently all their data ingestion and transformation pipelines used to be run in Pentaho (GUI-based). I had been tasked with fulfilling the transition from Pentaho to dbt.
        - Refactor and optimize python-based ingestion scripts for various sources including S3 and API endpoints.
        - Implement robust error handling to prevent run failures.
        - Translate Pentaho pipelines and models to modular SQL-based transformations that dbt uses.
        - Set up testing and data validation in dbt.
        - Set up CI/CD for local testing from docker containers and Postgres.
        - Manage dbt runs via Airflow DAGS.
        """
    },
    {
        "role": "Data Engineer",
        "company": "Digital Hive/ Azure Workshop",
        "dates": "03 2024 – 03 2024",
        "description": """
        For one of Digital Hives client that uses azure synapse I was tasked to give several workshops on how they could optimize their current data infrastructure. From layering in the data lake house to utilizing purview for data governance. Finally, we touched on Microsoft Fabric and compared the current setup benefits with the potential that Fabric offers.
        """
    },
    {
        "role": "Data Engineer",
        "company": "Digital Hive/Recruitment Script",
        "dates": "02 2024 – 02 2024",
        "description": """
        Recruitment Script (RS) is a Streamlit app that allows users to efficiently generate company-specific job postings and match candidates' CVs. When matching, relevant comments and questions for recruitment are also generated. I built this app in as a POC to demonstrate the potential of integrating OpenAI (ChatGPT) in to repetitive document based manual to automate and speed up processes.
        """
    },
    {
        "role": "Data Engineer",
        "company": "J&J/JO.E",
        "dates": "06 2023 – 01 2024",
        "description": """
        JO.E process Medical and Commercial sales data to generate insights and personalized recommendations. Using Kedro framework with the Apache Spark engine data is cleaned, processed, and restructured to be delivered to the data scientists that use it to generate the recommendations and train the model.
        - Intake and requirements management for ingestion and integration of novel data on S3 buckets in parquet files.
        - Set up and refactor nodes and pipelines for data processing in Kedro using Pyspark, pandas, polars.
        - Ensure codebase maturity for which to latest Spark version (date, datetime handling)
        - Detect inconsistencies in field naming over multiple layers to prevent Integrity Issues and ambiguity.
        - Maintain codebase and data quality through implementation on great expectations linting and unit testing.
        - Utilize ArgoCD to set up and monitor automated runs together with Bitbucket to manages streamlined CI/CD processing.
        - Closely align with sales force teams and business to layout needs and set up an implementation workflow.
        """
    },
    {
        "role": "Data Engineer",
        "company": "J&J/Data Capture Systems",
        "dates": "06 2022 – 04 2023",
        "description": """
        The data capture systems project was set up with the aim of gathering and harmonizing data from all laboratory processes executed at the R&D branch of J&J. A novel software developed by Dassault BIOVIA Compose was used to generate data capture interfaces for the laboratory processes performed by the analysts. Where before data was entered manually and prone to in consistencies and discordances all data would be collected following a pre-defined vocabulary using Collibra and read directly from the machines to be loaded into the data lake.
        - Develop and update laboratory processes using BIOVIA OneLab/Compose, and organize user friendly data capture interfaces for laboratory analysts.
        - Set up capture for the relevant data for every laboratory process execution to be ingested in the data lake.
        - Ensure that the digital protocol interface used by analysts in the lab captured the right data types that were correct and consistent over all other laboratory protocols.
        - Interact with laboratory analysts to convey data quality requirements and receive end user feedback.
        - Optimize workflow for digitalising the laboratory processes of various testing teams.
        - Integrate each compose protocol with CISPro to keep track of stock materials.
        - Train colleagues on laboratory processes and data BIOVIA Compose systems.
        """
    },
    {
        "role": "Data Engineer",
        "company": "Ordina/Data Transfer Automation Template",
        "dates": "03 2022 – 04 2022",
        "description": """
        Ordina aimed to develop a fully customizable ETL automation template. That would allow for minimal manual table and schema creations for the initial set up. Using T4 templates and autogenerated SSIS packages with Biml. The schemas and tables for each layer in the can be described in xml files that are read by Biml that together with T4 templates generate SSIS packages. These can then be used on premise on SSIS or migrated to ADF to be implemented in cloud solutions
        - Managed relational databases and implemented several ETL pipelines ADF and SSIS.
        - Aided in the data modelling for test implementations of the automation template
        """
    },
    {
        "role": "Data Engineer",
        "company": "Ordina/Data Visualization",
        "dates": "03 2022 – 04 2022",
        "description": """
        - Create OLTP diagram, and model a DWH in Azure.
        - Set up pipelines  in ADF for the cleaning and separation of raw data into cleansed and archived database schemas.
        - Generate dynamic PowerBI reports to visualize data and generate relevant KPI’s.
        """
    },
    {
        "role": "Research Scientist",
        "company": "KULeuven/Bone fracture healing",
        "dates": "09 2020 – 06 2021",
        "description": """
        Evaluate the biological processes involved in fracture healing and find possible bottlenecks in the healing process of old mice. These could lead to the development of new process-specific therapeutics to be used in humans.
        - Conducting a literature study in order to find the right packages and tools to process the data.
        - Applying the right controls on the acquired datasets.
        - Implementing the planned methods and tweaking them to the requirements where needed.
        - Perform statistical tests result in information relevant to the research questions.
        - Interpret and validate the results objectively.
        - Convey information in visualizations of the data and predictions.
        - Explain found results and their relation to the present field literature.
        """
    }
]

# Organize experiences by year
experience_by_year = defaultdict(list)
for exp in experience:
    start_year = exp["dates"].split(" ")[1]
    experience_by_year[start_year].append(exp)

# Sort years in descending order
sorted_years = sorted(experience_by_year.keys(), reverse=True)

# Dropdown for selecting the year
selected_year = st.selectbox("Select a year", sorted_years)

# Dropdown for selecting the experience if a year is selected
if selected_year:
    selected_experience = st.selectbox(
        "Select an experience",
        experience_by_year[selected_year],
        format_func=lambda x: f"{x['role']} at {x['company']}"
    )

    # Display the selected experience details
    st.subheader(selected_experience["role"])
    st.write(f"**Company:** {selected_experience['company']}")
    st.write(f"**Dates:** {selected_experience['dates']}")
    st.write(selected_experience["description"])
    
# Certifications Section
st.header("Certifications")
certifications = {
    "AWS": [("AWS certified cloud practitioner", "https://www.credly.com/badges/ddbdf1f6-4834-427a-823f-e50f8c25d8e9/public_url")],
    "Azure": [
        ("Azure fundamentals", "https://www.credly.com/badges/ed38066c-e15d-4210-9427-71873ccc5727?source=linked_in_profile"),
        ("Azure data fundamentals", "https://www.credly.com/badges/8ae50792-f82d-4c0b-9a8f-7628064a148a?source=linked_in_profile"),
        ("Azure data engineer associate", "https://www.credly.com/badges/164436b8-5d08-4758-b9af-1a3472148daf?source=linked_in_profile")
    ],
    "Python": [("PCEP certified entry-level python", "https://www.credly.com/badges/89c51e5d-b3be-4cef-bbdd-56ffae381e52?source=linked_in_profile")],
    "Databricks": [("Databricks Lakehouse fundamentals", "https://credentials.databricks.com/4035ed9e-59a3-4541-aa4b-7109202525c1")],
    "Snowflake": [("SnowPro Core Certificate", "https://achieve.snowflake.com/c1d2b6d0-0f70-490d-aa30-b36a4f4ad21a")],
    "dbt": [("dbt Fundamentals", "https://credentials.getdbt.com/f0985a9f-4b8e-4c02-9e3e-e14305b94a93#gs.c6rxlt")]
}

# Create tabs for each cloud provider
tabs = st.tabs(certifications.keys())
for tab, (provider, certs) in zip(tabs, certifications.items()):
    with tab:
        st.subheader(f"{provider} Certifications")
        for cert, link in certs:
            st.markdown(f"• [{cert}]({link})")

# Add a plot for coding languages experience
st.header("Coding Languages")
coding_experience = {
    "Python": 5,
    "SQL": 4,
    "R": 3,
    "Bash": 2
}
coding_df = pd.DataFrame(list(coding_experience.items()), columns=["Language", "Years of Experience"])

# Define custom color map
color_map = {"Python": "#0078D4", "SQL": "#FFD700", "R": "#800080", "Bash": "#FF0000"}

fig = px.bar(coding_df, x="Language", y="Years of Experience", title="Experience in Coding Languages",
             labels={"Years of Experience": "Years of Experience"}, color="Language",
             color_discrete_map=color_map)

fig.update_layout(
    xaxis_title="Language",
    yaxis_title="Years of Experience",
    plot_bgcolor='white',
    paper_bgcolor='white',
    font=dict(color='black')
)

st.plotly_chart(fig)

# Education Section
st.header("Education")

education = [
    {
        "degree": "Secondary diploma, Latin and Sciences",
        "institution": "Koninklijk Atheneum Maaseik",
        "dates": "2009 - 2015",
    },
    {
        "degree": "B.Sc. Biomedical Sciences",
        "institution": "Katholic University of Leuven",
        "dates": "2016 - 2019",
    },
    {
        "degree": "M.Sc. Biomedical Sciences",
        "institution": "Katholic University of Leuven",
        "dates": "2019 - 2021",
    },
]

# Organize education by start year
education_by_year = defaultdict(list)
for edu in education:
    start_year = edu["dates"].split(" - ")[0]
    education_by_year[start_year].append(edu)

# Sort years in descending order
sorted_years_edu = sorted(education_by_year.keys(), reverse=True)

# Dropdown for selecting the year
selected_year = st.selectbox("Select a year", sorted_years_edu)

# Display the selected education details
if selected_year:
    selected_education = education_by_year[selected_year][0]  # Assuming one education per year

    st.subheader(selected_education["degree"])
    st.write(f"**Institution:** {selected_education['institution']}")
    st.write(f"**Dates:** {selected_education['dates']}")

# Languages Section
st.header("Languages")
languages = {
    "English": "Native",
    "Circassian": "Native",
    "Dutch": "Native",
    "Arabic": "Professional",
    "French": "Basic",
    "Hebrew": "Basic"
}
st.write(pd.DataFrame(languages.items(), columns=["Language", "Proficiency"]))

# Contact Section
st.header("Contact")
st.write("**Email:** [aslan.hattukai@hotmail.com](mailto:aslan.hattukai@hotmail.com)")
st.write("**Tel:** +320470877633")
st.write("Feel free to reach out to me via [LinkedIn](https://www.linkedin.com/in/aslan-hattukai-6762421b5)")
