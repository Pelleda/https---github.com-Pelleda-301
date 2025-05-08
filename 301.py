import streamlit as st
import re

st.set_page_config(page_title="301 Redirect Manager")
st.title("🔀 301 Redirect Manager for .htaccess")

st.markdown("### Paste your old and new links in separate columns:")

col1, col2 = st.columns(2)
with col1:
    old_links = st.text_area("Old Links (one per line)", height=300, placeholder="/old-page-1\n/old-page-2\n/old-page-3")
with col2:
    new_links = st.text_area("New Links (one per line)", height=300, placeholder="/new-page-1\n/new-page-2\n/new-page-3")

generate_button = st.button("Generate .htaccess Redirects")

if generate_button:
    old_links_list = old_links.strip().split("\n")
    new_links_list = new_links.strip().split("\n")

    if len(old_links_list) != len(new_links_list):
        st.error("❗ The number of old links and new links must match.")
    else:
        redirects = []
        for old_link, new_link in zip(old_links_list, new_links_list):
            # Clean up the links, removing protocol and domain if present
            old_path = re.sub(r"https?://[^/]+", "", old_link).strip()
            new_path = re.sub(r"https?://[^/]+", "", new_link).strip()
            # Create the 301 redirect line
            redirects.append(f"Redirect 301 {old_path} {new_path}")
        # Display the result
        st.markdown("### 📄 Generated .htaccess Redirects:")
        st.code("\n".join(redirects))
