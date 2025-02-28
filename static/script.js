document.addEventListener("DOMContentLoaded", () => {
    const form = document.getElementById("summarize-form");
    const textInput = document.getElementById("text-input");
    const resultContainer = document.getElementById("result-container");
    const summaryDiv = document.getElementById("summary");
    const keywordsDiv = document.getElementById("keywords");

    form.addEventListener("submit", async (event) => {
        event.preventDefault(); // 阻止表單提交刷新頁面

        const formData = new FormData();
        formData.append("text", textInput.value);

        try {
            const response = await fetch("/summarize", {
                method: "POST",
                body: formData
            });

            if (!response.ok) {
                throw new Error("API 錯誤：" + response.statusText);
            }

            const data = await response.json();
            summaryDiv.innerHTML = "<p>" + data.summary.replace(/\n/g, "<br>") + "</p>"; 
            keywordsDiv.innerHTML = "<p>" + data.keywords.join(", ") + "</p>";

            resultContainer.style.display = "block"; // 顯示結果
        } catch (error) {
            console.error("錯誤：", error);
            summaryDiv.innerHTML = "<p style='color: red;'>處理失敗，請稍後再試</p>";
            keywordsDiv.innerHTML = "";
            resultContainer.style.display = "block";
        }
    });
});



