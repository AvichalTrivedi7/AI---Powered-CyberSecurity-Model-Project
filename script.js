async function sendCommand(command) {
  const logList = document.getElementById("logList");
  const llmState = document.getElementById("llmState");
  
  llmState.textContent = "LLM: thinking...";
  
  try {
    const response = await fetch("http://127.0.0.1:5000/classify", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ command })
    });
    
    const result = await response.json();
    llmState.textContent = "LLM: done";
    
    const entry = document.createElement("div");
    entry.className = "log-entry";
    entry.innerHTML = `
      <span class="log-entry__tag">${command}</span>
      <span>${result.classification}</span>
    `;
    logList.prepend(entry);
    
    // Update door state only if valid normal
    if (result.classification.includes("Valid") && result.classification.includes("Normal")) {
      if (command === "open_door") {
        document.getElementById("door").dataset.state = "open";
        document.getElementById("doorState").textContent = "Door: OPEN";
      } else if (command === "close_door") {
        document.getElementById("door").dataset.state = "closed";
        document.getElementById("doorState").textContent = "Door: CLOSED";
      }
    }
    
  } catch (err) {
    llmState.textContent = "LLM: error";
    console.error(err);
  }
}

document.getElementById("openBtn").addEventListener("click", () => sendCommand("open_door"));
document.getElementById("closeBtn").addEventListener("click", () => sendCommand("close_door"));
// NEW: custom command sender
document.getElementById("customBtn").addEventListener("click", () => {
  const input = document.getElementById("customInput");
  const command = input.value.trim();
  if (command) {
    sendCommand(command);
    input.value = ""; // clear after sending
  }
});
