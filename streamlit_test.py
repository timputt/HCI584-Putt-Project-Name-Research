
import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# callback for plotting
def make_plot():
        fig, ax = plt.subplots(figsize=(18, 4)) # make figure and axis
        
        # TODO: from the list of strings in ng_str_list, make a list with pairs like name_lst
        ng_str_list = st.session_state.name_selection
        print(ng_str_list)

        # Name/gender as a list, many of these
        name_lst = [["James","M"], 
            ["John","M"],
            ["Jonathan","M"],
            ["John","F"]
        ]

        for nd in name_lst:
            name = nd[0]
            gender = nd[1]
            dfn = st.session_state.df.query('Name == @name and Gender==@gender')
            total = dfn["Count"].sum()

            st.write(f"{name} ({gender}): {total} total hits")

            # in order to accumulate multiple lines, you must use ax.plot() not plt.plot()! 
            ax.plot( 'Year', 'Count', data=dfn, 
                linewidth=2,
                label=name+","+gender)

        # show legend
        plt.legend()
        plt.xlim(1880, 2020) #

        plt.yscale('log') # log scale makes more sense to me ...

        # plot figure with its axis 
        st.pyplot(fig)

def main():
    df, df_name_stats = load_data()
    st.session_state.df = df # make df accessible from callback
    page = st.sidebar.selectbox("Choose a page", ["Tableview", "Exploration"])

    if page == "Tableview":
        st.header("Most popular names 1880-202")
        st.write(df_name_stats)
        
    elif page == "Exploration":
        st.title("Data Exploration")

        # make a list with "Name, Gender" 
        ng_as_str_lst = []
        for n,g in zip(df_name_stats["Name"], df_name_stats["Gender"]):
            ng_as_str_lst.append(n + ", " + g)


        names_sel = st.multiselect("Select some names:", ng_as_str_lst)
        print(names_sel)

        st.session_state.name_selection = names_sel # make a global var called name_selection that we can access in the callback

        st.button("Make plot", key=None, help=None, on_click=make_plot, args=None, kwargs=None)
        

@st.cache
def load_data():
    df = pd.read_csv("ssn_files/all_years.csv")
    df_name_stats = pd.read_csv("name_stats.csv")
    df_name_stats.sort_values(by="Count", inplace=True, ascending=False) # sort internally by Count, descending
    df_name_stats.reset_index(drop=True, inplace=True) # re-index
    df_name_stats = df_name_stats.loc[:100] # only use  X most popular names, otherwise streamlit chokes ...
    return df, df_name_stats


if __name__ == "__main__":
    main()