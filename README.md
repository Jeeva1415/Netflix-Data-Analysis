# 🎬 Netflix Data Analysis

A Python data analysis project that explores the Netflix titles dataset with **Pandas** and **Matplotlib**. It filters the catalog down to movies released between 2000 and 2020 and visualizes how the number of movies on Netflix changed over those two decades.

---

## Dataset

- **Source:** Collected from [Kaggle](https://www.kaggle.com/)
- **File:** `netflix_titles.csv`
- **Size:** 8,807 titles (6,131 movies and 2,676 TV shows)
- **Columns (12):** `show_id`, `type`, `title`, `director`, `cast`, `country`, `date_added`, `release_year`, `rating`, `duration`, `listed_in`, `description`
- **Release years covered:** 1925 to 2021

---

## What This Project Does

1. Loads the dataset with Pandas.
2. Filters the data to **movies only** (`type == 'Movie'`).
3. Keeps movies with a **release year from 2000 to 2020** (5,378 movies).
4. Plots a **histogram** of release years with Matplotlib.

---

## Key Findings

- Of the 6,131 movies in the dataset, **5,378 (about 88%)** were released between 2000 and 2020.
- Movie counts grow slowly through the 2000s (33 movies in 2000, 154 in 2010).
- There is a **sharp rise after 2014**, from 264 movies in 2014 to 658 in 2016.
- The peak is **767 movies in both 2017 and 2018**.
- Counts then drop to 633 in 2019 and 517 in 2020. This may reflect the dataset's coverage of recent releases rather than a real decline.

---

## Tech Stack

![Python](https://img.shields.io/badge/-Python-3776AB?style=flat-square&logo=python&logoColor=white)
![Pandas](https://img.shields.io/badge/-Pandas-150458?style=flat-square&logo=pandas&logoColor=white)
![Matplotlib](https://img.shields.io/badge/-Matplotlib-11557C?style=flat-square&logo=plotly&logoColor=white)

---

## Project Structure

```
Netflix_Data_Analysis/
├── Netflix.py           # Analysis and visualization script
├── netflix_titles.csv   # Dataset
└── README.md
```

---

## Future Improvements

- [ ] Handle missing values in `director`, `cast`, `country`, and `date_added`
- [ ] Compare movies vs. TV shows over time
- [ ] Analyze the most common genres (`listed_in`) and ratings
- [ ] Find top countries producing Netflix content
- [ ] Analyze movie duration trends
- [ ] Build an interactive dashboard with Power BI or Streamlit

---

## Author

**Jeevaneshwaran G**
[GitHub](https://github.com/Jeeva1415) · [LinkedIn](https://www.linkedin.com/in/jeevaneshwaran-g-a05863315)

---

*Turning data into insights.* 🎬
