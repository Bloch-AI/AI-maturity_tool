# AI Feasibility Assessment Tool

A Streamlit application for assessing AI prototype/MVP ideas across 4 key dimensions to determine project feasibility for a 10-week timeframe.

## Features

- **4 Assessment Dimensions:**
  - Technical Feasibility
  - Business Feasibility  
  - Resource Feasibility
  - Data Availability & Quality

- **Interactive Scoring:** 
  - 1-5 scale for each dimension
  - Complete scoring criteria displayed for all scores (1-5)
  - Visual highlighting of selected score

- **Automated Categorization:** Based on total score (out of 20):
  - 15-20: High Feasibility
  - 12-14: Moderate Feasibility
  - Below 12: Prototype Focus

- **Professional Dashboard:**
  - Radar chart visualization of dimension scores
  - Progress bars for each dimension
  - Color-coded result categories
  - Clear, actionable recommendations
  - Clean, professional interface without distracting elements

## Installation

1. Install Python 3.8 or higher
2. Install dependencies:
```bash
pip install -r requirements.txt
```

## Running the App

```bash
streamlit run ai_feasibility_assessment.py
```

The app will open in your browser at `http://localhost:8501`

## How to Use

1. **Rate each dimension** using the sliders (1-5 scale)
2. **Review the descriptions** that appear for scores 1, 3, and 5
3. **Click "Calculate Feasibility Score"** to see results
4. **Review your assessment:**
   - Total score and category
   - Radar chart visualization
   - Recommended actions
   - Detailed breakdown by dimension
5. **Start a new assessment** using the reset button if needed

## Scoring Guide

### Technical Feasibility
- **Score 1:** Requires specialist systems or significant new technical skills
- **Score 2:** Needs substantial learning curve and new tool adoption
- **Score 3:** Achievable with some learning or adaptation
- **Score 4:** Mostly familiar tools with minor new elements
- **Score 5:** Implementable with accessible tools (ChatGPT, Copilot, n8n)

### Business Feasibility
- **Score 1:** Interesting concept but limited business relevance or measurable benefit
- **Score 2:** Some potential value but unclear business case
- **Score 3:** Partially aligned to goals with clear value potential
- **Score 4:** Well-aligned with strategic goals and demonstrable benefits
- **Score 5:** Directly supports strategic priority with clear ROI potential

### Resource Feasibility
- **Score 1:** One individual with limited time; other commitments dominate
- **Score 2:** Single person with moderate availability
- **Score 3:** Some dedicated time, but delivery may be challenging
- **Score 4:** Good team availability with mostly clear schedules
- **Score 5:** Team of two or more with sufficient time and clear roles

### Data Availability & Quality
- **Score 1:** Little relevant data available or poor quality/unstructured data
- **Score 2:** Limited data requiring significant processing
- **Score 3:** Partial access; some data cleaning or preparation required
- **Score 4:** Good data availability with minor preparation needed
- **Score 5:** Well-structured data readily available for immediate use

## Important Note

This framework is **not an assessment of merit or ambition**. Lower-scoring projects are often the most innovative and transformative. The purpose is to help participants calibrate scope and manage expectations from the outset, ensuring realistic delivery plans.

## License MIT
