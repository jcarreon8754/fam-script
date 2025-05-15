import streamlit as st
from datetime import datetime

st.title("Hello Familia")

name = st.text_input("Enter your name chief:", value="").strip().lower()
wife = 'sarah'

current_datetime = datetime.now()
current_normalized_time = current_datetime.strftime("%H:%M")

if name:
    if 'juan' in name:
        st.write("Hello big dawg")

    elif wife in name:
        st.write("Hello bb cheeks")
        kisses = st.radio('Have you given besitos?', ["---select an option---", 'of course', 'no...'], index=None, key='kisses')
        if kisses:
            if kisses == 'of course':
                st.write('Love you bb')
            else:
                st.write('Look at camera and give me besitos')
            st.write('Thanks for your besitos')

            love = st.radio("---select an option---", 'Do you still love me?', ['i guess so', 'nahh'], index=None, key='love')
            if love == 'i guess so':
                much = st.number_input('How much? (enter number)', min_value=0, key='much')
                if much >= 99:
                    st.write('Yayyy you love me mucho. I also love you mucho')
                else:
                    st.write("You don't love me mucho")
            else:
                st.write('Oh, ok...')
                st.write('That hurts')


    elif 'jose' in name or 'rocio' in name:
        st.write('Hello parent')
        food = st.radio('Did you eat soup today?', ["---select an option---", 'claro', 'hell no'], index=None, key='food')
        if food == 'claro':
            st.write('Gross')
        else:
            st.write('Good!')

        work = st.radio('Are you working?', ['yes', 'no'], index=None, key='work')
        if work == 'yes':
            st.write('Okie, keep at it! Love you always')
        else:
            st.write('Very nice, love you always!!!')

    elif 'sofia' in name:
        st.write('Hello seester')
        bf = st.radio('Is Cole still there?', ['yes', 'no'], index=None, key='bf')
        if bf == 'yes':
            st.write('Booo make him leave')
        else:
            st.write('Nice lol')

        classes = st.number_input('How many classes do you have today?', min_value=0, key='classes')
        if classes <= 2:
            st.write('Ok not bad, love you')
        else:
            st.write('Oof, good luck chief, love you')

    elif any(n in name for n in ['natalie', 'natty', 'nanga']):
        st.write('Hello nangana')
        sleep = st.radio('Have you woken up yet?', ['yes', 'no'], index=None, key='sleep')
        if sleep == 'yes':
            st.write('Finally')
            studying = st.number_input('How many hours have you studied for STEP today?', min_value=0, key='studying')
            if studying <= 3:
                st.write('Those are rookie numbers')
            elif 3 < studying <= 5:
                st.write("That's not very good nangana, moreeeeeeee")
            else:
                st.write('Ok, not bad, keep the grind going')
        else:
            st.write(f'Dawg, gotta get up, it is {current_normalized_time}')

    elif any(n in name for n in ['carreon', 'samaranayake', 'duenas', 'jacome']):
        st.write('Hello family, access granted')

    elif 'cole' in name:
        chickens = st.number_input('How many chickens have you offered?', min_value=0, key='chickens')
        if chickens > 1e25:
            st.write('You good')
        else:
            st.write('You shall not pass')

    else:
        st.write('Who tf is this, gtfoh')
