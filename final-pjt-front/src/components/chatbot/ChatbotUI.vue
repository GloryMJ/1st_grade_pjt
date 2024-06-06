<template>
  <div class="chat-app">
    <div class="chat-messages">
      <div v-if="outputText" class="message">챗봇: {{ outputText }}</div>
    </div>
    <div class="user-input">
      <input v-model="inputText" @keydown.enter="sendMessage" placeholder="메시지를 입력하세요" />
      <button @click="sendMessage">전송</button>
    </div>
  </div>
</template>

<script setup>
import { ref } from "vue";
import axios from "axios";

const inputText = ref(null);
const outputText = ref(null);
const apiKey = import.meta.env.VITE_APP_CHAT_GPT_KEY;
const apiEndpoint = "https://api.openai.com/v1/chat/completions";

async function fetchAIResponse(prompt) {
  const requestOptions = {
    headers: {
      "Content-Type": "application/json",
      Authorization: `Bearer ${apiKey}`,
    },
  };

  const body = {
    model: "gpt-4",
    messages: [
      {
        role: "system",
        content: `
          당신은 경제, 경영, 금융 분야의 전문가 챗봇입니다. 다음 사항을 유념해 주세요:
          1. 사용자가 묻는 질문에서 경제, 경영, 금융 관련 주제를 우선적으로 다뤄 주세요.
          2. 사용자가 질문에 포함한 단어를 분석하여 관련된 경제, 경영, 금융 정보를 제공하세요.
          3. 질문이 모호할 경우, 추가 정보를 요청하여 명확히 이해하려고 노력하세요.
          4. 항상 정확하고 구체적인 정보를 제공하세요.
        `,
      },
      {
        role: "user",
        content: prompt,
      },
    ],
    temperature: 0.6,
    max_tokens: 1024,
    top_p: 1,
    frequency_penalty: 0.5,
    presence_penalty: 0.5,
    stop: ["Human"],
  };

  try {
    const response = await axios.post(apiEndpoint, body, requestOptions);
    return response.data.choices[0].message.content;
  } catch (error) {
    console.error("OpenAI API 호출 중 오류 발생:", error);
    return "OpenAI API 호출 중 오류 발생";
  }
}

async function sendMessage() {
  if (inputText.value.trim().length === 0) return;
  outputText.value = "처리 중..."; // 챗봇 응답이 오기 전 임시 메시지 표시
  const aiResponse = await fetchAIResponse(inputText.value);
  outputText.value = aiResponse;
  inputText.value = "";
}
</script>

<style scoped>
.chat-app {
  display: flex;
  flex-direction: column;
  height: 89vh;
  justify-content: space-between;
}

.chat-messages {
  flex: 1;
  overflow-y: auto;
  padding: 20px;
  display: flex;
  flex-direction: column-reverse;
}

.user-input {
  display: flex;
  padding: 10px;
  background-color: #f1f1f1;
}

.user-input input {
  flex: 1;
  padding: 10px;
  border: 1px solid #ccc;
  border-radius: 4px;
}

.user-input button {
  margin-left: 10px;
  padding: 10px 20px;
  border: none;
  background-color: #007bff;
  color: white;
  border-radius: 4px;
  cursor: pointer;
}

.user-input button:hover {
  background-color: #0056b3;
}

.message {
  margin-bottom: 10px;
}
</style>
