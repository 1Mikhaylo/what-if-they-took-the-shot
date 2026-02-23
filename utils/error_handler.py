import streamlit as st
import functools

def handle_errors(func):
    """Decorator to catch and display errors gracefully."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except FileNotFoundError as e:
            st.error(f"❌ Data file not found: {str(e)}")
            st.info("Please ensure all data files are in the correct location.")
            return None
        except KeyError as e:
            st.error(f"❌ Player not found in dataset: {str(e)}")
            st.info("This player may not have sufficient data for analysis.")
            return None
        except Exception as e:
            st.error(f"❌ An unexpected error occurred: {str(e)}")
            st.info("Please try again or contact support if the issue persists.")
            return None
    return wrapper
