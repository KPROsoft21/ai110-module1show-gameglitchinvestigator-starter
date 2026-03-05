# 💭 Reflection: Game Glitch Investigator

Answer each question in 3 to 5 sentences. Be specific and honest about what actually happened while you worked. This is about your process, not trying to sound perfect.

## 1. What was broken when you started?

- What did the game look like the first time you ran it?
- List at least two concrete bugs you noticed at the start  
  (for example: "the secret number kept changing" or "the hints were backwards").
  #FIX: It said return "Too High", "📉 Go Higher!" if guess > and "Too Low", "📈 Go LOWER!" if lower
  #FIX: New Game button doesn't work
  #FIX: when I guess 100 twice it goes from go lower to go higher

---

## 2. How did you use AI as a teammate?

- Which AI tools did you use on this project (for example: ChatGPT, Gemini, Copilot)? Copilot
- Give one example of an AI suggestion that was correct (including what the AI suggested and how you verified the result). 
It found where to fix the new game button
- Give one example of an AI suggestion that was incorrect or misleading (including what the AI suggested and how you verified the result).
It takes tangents if I write a comment like the FIXME comments even if I fix it

---

## 3. Debugging and testing your fixes

- How did you decide whether a bug was really fixed?
I ran a test case to see if it fixed it
- Describe at least one test you ran (manual or using pytest)  
  and what it showed you about your code.
  I tried to repeatedly guess 100 and it switched its answer
- Did AI help you design or understand any tests? How?
Yes, instead of finding the bugs myself it found the issues for me

---

## 4. What did you learn about Streamlit and state?

- In your own words, explain why the secret number kept changing in the original app.
  The secret number kept changing because Streamlit reruns the script from top to bottom every time a user interacts with the app. Without using Streamlit's session state to persist the secret number, it gets reinitialized on every rerun, leading to a new random number being generated.
- How would you explain Streamlit "reruns" and session state to a friend who has never used Streamlit?
  Streamlit "reruns" the entire script from top to bottom whenever a user interacts with the app, such as clicking a button or changing an input. This ensures the app stays responsive and updates dynamically. However, this behavior can reset variables unless they are stored in Streamlit's session state, which acts like a persistent dictionary to retain values across reruns.
- What change did you make that finally gave the game a stable secret number?
The change that finally gave the game a stable secret number was using Streamlit's st.session_state to store the secret number. By initializing the secret number in st.session_state and checking if it already exists before generating a new one, the value persisted across reruns of the script, preventing it from being reset on every user interaction.


## 5. Looking ahead: your developer habits

- What is one habit or strategy from this project that you want to reuse in future labs or projects? 
  - This could be a testing habit, a prompting strategy, or a way you used Git.
  Find bugs with the AI
- What is one thing you would do differently next time you work with AI on a coding task?
Check if it fixed the bug
- In one or two sentences, describe how this project changed the way you think about AI generated code.
  This project showed me that while AI can be a powerful tool for identifying and fixing bugs. It requires careful verification and testing to ensure the changes are correct. It reinforced the importance of understanding the code and not relying solely on AI suggestions.

