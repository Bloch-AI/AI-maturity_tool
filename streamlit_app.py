import streamlit as st
import plotly.graph_objects as go
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="AI Feasibility Assessment",
    page_icon="📊",
    layout="wide"
)

# Custom CSS for better styling
st.markdown("""
    <style>
    .main-header {
        font-size: 2.5rem;
        font-weight: bold;
        color: #1e3a5f;
        text-align: center;
        margin-bottom: 0.5rem;
    }
    .sub-header {
        font-size: 1.2rem;
        color: #666;
        text-align: center;
        margin-bottom: 2rem;
    }
    .dimension-title {
        font-size: 1.3rem;
        font-weight: bold;
        color: #1e3a5f;
        margin-bottom: 0.5rem;
    }
    .dimension-description {
        font-size: 0.95rem;
        color: #555;
        margin-bottom: 1rem;
    }
    .score-criteria {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 8px;
        margin-top: 1rem;
        font-size: 0.9rem;
    }
    .score-item {
        padding: 0.3rem 0;
        border-bottom: 1px solid #e0e0e0;
    }
    .score-item:last-child {
        border-bottom: none;
    }
    .score-selected {
        color: #dc3545;
        font-weight: bold;
    }
    .result-box {
        padding: 2rem;
        border-radius: 10px;
        margin-top: 2rem;
        text-align: center;
    }
    .high-feasibility {
        background-color: #d4edda;
        border: 2px solid #28a745;
    }
    .moderate-feasibility {
        background-color: #d1ecf1;
        border: 2px solid #17a2b8;
    }
    .prototype-focus {
        background-color: #fff3cd;
        border: 2px solid #ffc107;
    }
    </style>
""", unsafe_allow_html=True)

# Title
st.markdown('<h1 class="main-header">AI Feasibility Assessment Framework</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-header">Evaluate your AI project across 4 key dimensions to determine the appropriate scope for a 10-week timeframe</p>', unsafe_allow_html=True)

# Initialize session state
if 'show_results' not in st.session_state:
    st.session_state.show_results = False
if 'scores' not in st.session_state:
    st.session_state.scores = {}

# Create columns for the assessment
col1, col2 = st.columns(2)

# Define scoring descriptions with all criteria
dimensions = {
    'Technical Feasibility': {
        'description': 'Assesses whether required technology and tools are readily available and within the team\'s current capability.',
        'scores': {
            1: 'Requires specialist systems or significant new technical skills',
            2: 'Needs substantial learning curve and new tool adoption',
            3: 'Achievable with some learning or adaptation',
            4: 'Mostly familiar tools with minor new elements',
            5: 'Implementable with accessible tools (ChatGPT, Copilot, n8n)'
        }
    },
    'Business Feasibility': {
        'description': 'Considers alignment with business goals and expected value delivery.',
        'scores': {
            1: 'Interesting concept but limited business relevance or measurable benefit',
            2: 'Some potential value but unclear business case',
            3: 'Partially aligned to goals with clear value potential',
            4: 'Well-aligned with strategic goals and demonstrable benefits',
            5: 'Directly supports strategic priority with clear ROI potential'
        }
    },
    'Resource Feasibility': {
        'description': 'Evaluates whether the team has sufficient time, people, and attention to deliver during the Bootcamp.',
        'scores': {
            1: 'One individual with limited time; other commitments dominate',
            2: 'Single person with moderate availability',
            3: 'Some dedicated time, but delivery may be challenging',
            4: 'Good team availability with mostly clear schedules',
            5: 'Team of two or more with sufficient time and clear roles'
        }
    },
    'Data Availability & Quality': {
        'description': 'Evaluates whether required data exists, is accessible, and of usable standard.',
        'scores': {
            1: 'Little relevant data available or poor quality/unstructured data',
            2: 'Limited data requiring significant processing',
            3: 'Partial access; some data cleaning or preparation required',
            4: 'Good data availability with minor preparation needed',
            5: 'Well-structured data readily available for immediate use'
        }
    }
}

# Create the assessment form
with st.form("assessment_form"):
    st.markdown("### Rate Each Dimension (1-5)")
    st.info("Score each dimension based on your project's current state. All scoring criteria are shown below each slider to guide your assessment.")
    st.markdown("---")
    
    scores = {}
    
    # Technical Feasibility
    with col1:
        st.markdown(f"<div class='dimension-title'>Technical Feasibility</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='dimension-description'>{dimensions['Technical Feasibility']['description']}</div>", unsafe_allow_html=True)
        
        technical_score = st.select_slider(
            "Select score for Technical Feasibility",
            options=[1, 2, 3, 4, 5],
            value=3,
            key="technical",
            label_visibility="collapsed"
        )
        scores['Technical Feasibility'] = technical_score
        
        # Show all scoring criteria
        st.markdown("<div class='score-criteria'>", unsafe_allow_html=True)
        for score, desc in dimensions['Technical Feasibility']['scores'].items():
            if score == technical_score:
                st.markdown(f"<div class='score-item score-selected'>Score {score} (Selected): {desc}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='score-item'><strong>Score {score}:</strong> {desc}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Resource Feasibility
        st.markdown(f"<div class='dimension-title'>Resource Feasibility</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='dimension-description'>{dimensions['Resource Feasibility']['description']}</div>", unsafe_allow_html=True)
        
        resource_score = st.select_slider(
            "Select score for Resource Feasibility",
            options=[1, 2, 3, 4, 5],
            value=3,
            key="resource",
            label_visibility="collapsed"
        )
        scores['Resource Feasibility'] = resource_score
        
        # Show all scoring criteria
        st.markdown("<div class='score-criteria'>", unsafe_allow_html=True)
        for score, desc in dimensions['Resource Feasibility']['scores'].items():
            if score == resource_score:
                st.markdown(f"<div class='score-item score-selected'>Score {score} (Selected): {desc}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='score-item'><strong>Score {score}:</strong> {desc}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Business Feasibility and Data Quality
    with col2:
        st.markdown(f"<div class='dimension-title'>Business Feasibility</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='dimension-description'>{dimensions['Business Feasibility']['description']}</div>", unsafe_allow_html=True)
        
        business_score = st.select_slider(
            "Select score for Business Feasibility",
            options=[1, 2, 3, 4, 5],
            value=3,
            key="business",
            label_visibility="collapsed"
        )
        scores['Business Feasibility'] = business_score
        
        # Show all scoring criteria
        st.markdown("<div class='score-criteria'>", unsafe_allow_html=True)
        for score, desc in dimensions['Business Feasibility']['scores'].items():
            if score == business_score:
                st.markdown(f"<div class='score-item score-selected'>Score {score} (Selected): {desc}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='score-item'><strong>Score {score}:</strong> {desc}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
        
        st.markdown("---")
        
        # Data Availability & Quality
        st.markdown(f"<div class='dimension-title'>Data Availability & Quality</div>", unsafe_allow_html=True)
        st.markdown(f"<div class='dimension-description'>{dimensions['Data Availability & Quality']['description']}</div>", unsafe_allow_html=True)
        
        data_score = st.select_slider(
            "Select score for Data Availability & Quality",
            options=[1, 2, 3, 4, 5],
            value=3,
            key="data",
            label_visibility="collapsed"
        )
        scores['Data Availability & Quality'] = data_score
        
        # Show all scoring criteria
        st.markdown("<div class='score-criteria'>", unsafe_allow_html=True)
        for score, desc in dimensions['Data Availability & Quality']['scores'].items():
            if score == data_score:
                st.markdown(f"<div class='score-item score-selected'>Score {score} (Selected): {desc}</div>", unsafe_allow_html=True)
            else:
                st.markdown(f"<div class='score-item'><strong>Score {score}:</strong> {desc}</div>", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)
    
    # Instructions before submit button
    st.markdown("---")
    st.markdown("**Score your use case. Is it feasible? Are we targeting a working solution or prototype?**")
    
    # Submit button
    submitted = st.form_submit_button("Calculate Feasibility Score", type="primary", use_container_width=True)
    
    if submitted:
        st.session_state.scores = scores
        st.session_state.show_results = True

# Display results if form has been submitted
if st.session_state.show_results:
    total_score = sum(st.session_state.scores.values())
    
    # Determine feasibility category
    if total_score >= 15:
        category = "High Feasibility"
        category_class = "high-feasibility"
        recommendations = [
            "Aim for full feature implementation",
            "Focus on user experience and refinement",
            "Plan for stakeholder demonstrations"
        ]
        description = "The project is well-suited for a more complete solution within the 10-week timeframe. Teams can pursue comprehensive functionality and polished deliverables."
    elif total_score >= 12:
        category = "Moderate Feasibility"
        category_class = "moderate-feasibility"
        recommendations = [
            "Consider reducing initial scope",
            "Identify areas requiring facilitator support",
            "Build in contingency planning"
        ]
        description = "The project is viable but may require some simplification or additional support. Teams should identify potential challenges early and develop mitigation strategies."
    else:
        category = "Prototype Focus"
        category_class = "prototype-focus"
        recommendations = [
            "Focus on core concept validation",
            "Create proof-of-concept demonstration",
            "Document learnings for future development"
        ]
        description = "The team should aim for a minimum viable product (MVP) or demonstration concept. This approach allows exploration of innovative ideas whilst maintaining realistic delivery expectations."
    
    # Results section
    st.markdown("---")
    st.markdown("## Assessment Results")
    
    # Score breakdown
    col_score, col_chart = st.columns([1, 1])
    
    with col_score:
        st.markdown(f"""
            <div class="result-box {category_class}">
                <h2>{category}</h2>
                <h1 style="font-size: 3rem; margin: 1rem 0;">{total_score}/20</h1>
                <p>{description}</p>
            </div>
        """, unsafe_allow_html=True)
        
        # Recommendations
        st.markdown("### Recommended Actions")
        for rec in recommendations:
            st.markdown(f"• {rec}")
    
    with col_chart:
        # Create radar chart
        fig = go.Figure()
        
        categories = list(st.session_state.scores.keys())
        values = list(st.session_state.scores.values())
        values.append(values[0])  # Complete the circle
        categories.append(categories[0])
        
        fig.add_trace(go.Scatterpolar(
            r=values,
            theta=categories,
            fill='toself',
            name='Your Score',
            fillcolor='rgba(30, 58, 95, 0.3)',
            line=dict(color='#1e3a5f', width=2)
        ))
        
        fig.update_layout(
            polar=dict(
                radialaxis=dict(
                    visible=True,
                    range=[0, 5],
                    tickmode='array',
                    tickvals=[1, 2, 3, 4, 5]
                )),
            showlegend=False,
            title="Dimension Scores",
            height=400
        )
        
        st.plotly_chart(fig, use_container_width=True)
    
    # Detailed breakdown
    st.markdown("### Detailed Score Breakdown")
    
    df_scores = pd.DataFrame([
        {"Dimension": dim, "Score": score, "Max": 5}
        for dim, score in st.session_state.scores.items()
    ])
    
    col_table1, col_table2 = st.columns(2)
    with col_table1:
        for i in range(0, 2):
            dim = list(st.session_state.scores.keys())[i]
            score = st.session_state.scores[dim]
            progress = score / 5
            st.metric(dim, f"{score}/5")
            st.progress(progress)
    
    with col_table2:
        for i in range(2, 4):
            dim = list(st.session_state.scores.keys())[i]
            score = st.session_state.scores[dim]
            progress = score / 5
            st.metric(dim, f"{score}/5")
            st.progress(progress)
    
    # Important note
    st.info("""
        **Important:** This framework is **not an assessment of merit or ambition**. Lower-scoring projects are often the most 
        innovative and transformative. The purpose is to help participants calibrate scope and manage expectations from the 
        outset, ensuring realistic delivery plans.
    """)
    
    # Reset button
    if st.button("Start New Assessment", type="secondary"):
        st.session_state.show_results = False
        st.session_state.scores = {}
        st.rerun()

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center; color: #666; font-size: 0.9rem;'>
        <p style='margin-top: 2rem;'>© ESTU Global 2025</p>
    </div>
""", unsafe_allow_html=True)
