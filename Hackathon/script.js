const timelineContainer = document.getElementById("timeline-container");
const weekDetails = document.getElementById("week-details");
const reportStatus = document.getElementById("report-status");
const suggestionsContainer = document.getElementById("suggestions");
const savedNotesContainer = document.getElementById("saved-notes");

const timelineData = Array.from({ length: 10 }, (_, i) => ({
  week: i + 1,
  event: i + 1 === 5 ? "Midterm Exams" : i + 1 === 10 ? "Final Exams" : `Week ${i + 1}`
}));

const assignmentsData = {
  1: [
    { name: "AI Basics", startDate: "2025-04-01", dueDate: "2025-04-07", endDate: "2025-04-07", done: true },
    { name: "Data Science Intro", startDate: "2025-04-02", dueDate: "2025-04-08", endDate: "", done: false },
  ],
  5: [
    { name: "Midterm Preparation", startDate: "2025-05-01", dueDate: "2025-05-05", endDate: "2025-05-05", done: true },
  ],
  10: [
    { name: "Final Project Submission", startDate: "2025-05-20", dueDate: "2025-05-30", endDate: "", done: false },
  ],
};

function renderTimeline() {
  timelineData.forEach((item) => {
    const div = document.createElement("div");
    div.classList.add("timeline-item");
    if (item.week === 5) div.classList.add("midterm");
    if (item.week === 10) div.classList.add("final");

    div.innerText = `Week ${item.week}`;
    div.addEventListener("click", () => showWeekDetails(item.week, div));
    timelineContainer.appendChild(div);
  });
}

function showWeekDetails(week, element) {
  document.querySelectorAll(".timeline-item").forEach((item) => {
    item.classList.remove("active");
  });
  element.classList.add("active");

  const weekAssignments = assignmentsData[week].map((a) => `
    <tr class="${a.done ? 'done' : a.endDate ? '' : 'missing-end-date'}">
      <td>${a.name}</td>
      <td>${a.startDate}</td>
      <td>${a.dueDate}</td>
      <td>${a.endDate || 'Not Completed'}</td>
    </tr>
  `).join('');

  weekDetails.innerHTML = `
    <h3>Week ${week}</h3>
    <table>
      <thead>
        <tr>
          <th>Assignment Name</th>
          <th>Start Date</th>
          <th>Due Date</th>
          <th>End Date</th>
        </tr>
      </thead>
      <tbody>
        ${weekAssignments}
      </tbody>
    </table>
  `;

  renderSuggestions(week);
}

function renderSuggestions(week) {
  suggestionsContainer.innerHTML = `
    <h3>Study Suggestions for Week ${week}</h3>
    <p>Focus on completing remaining assignments and allocate study hours for exams.</p>
  `;
}

document.getElementById("generate-report").addEventListener("click", () => {
  reportStatus.innerText = "Weekly Report Generated and Sent to Email!";
});

document.getElementById("save-notes").addEventListener("click", () => {
  const notes = document.getElementById("note-taking").value;
  savedNotesContainer.innerText = `Saved Notes: ${notes}`;
});

renderTimeline();
