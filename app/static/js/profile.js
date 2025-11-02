(function () {
    const view = document.getElementById('viewMode');
    const form = document.getElementById('editMode');
    const alertBox = document.getElementById('alert');
  
    const fields = ["symptoms","medications","conditions","allergies","surgeries","vaccines","family"];
    const v = id => document.getElementById(`v-${id}`); // view, shortened for convenience
    const f = id => document.getElementById(`f-${id}`); // form, editing mode
  
    function show(el){ el.hidden = false; }
    function hide(el){ el.hidden = true; }
    function msg(text, kind="info"){
      alertBox.textContent = text || "";
      alertBox.className = kind === "error" ? "bg-red-100 p-2" :
                           kind === "ok"    ? "bg-green-100 p-2" : "";
    }
  
    async function loadProfile() {
      const res = await fetch('/profile/data', { credentials: 'same-origin' });
      const data = await res.json(); // TODO: determine if need get_json()?
      if (!res.ok) { msg(data.error || "Failed to load profile", "error"); return; }
  
      // fill view
      v("symptoms").textContent   = data.symptoms || "";
      v("medications").textContent= data.medications || "";
      v("conditions").textContent = data.conditions || "";
      v("allergies").textContent  = data.allergies || "";
      v("surgeries").textContent  = data.surgeries || "";
      v("vaccines").textContent   = data.vaccines || "";
      v("family").textContent     = data.family_history || "";
  
      // fill form
      f("symptoms").value   = data.symptoms || "";
      f("medications").value= data.medications || "";
      f("conditions").value = data.conditions || "";
      f("allergies").value  = data.allergies || "";
      f("surgeries").value  = data.surgeries || "";
      f("vaccines").value   = data.vaccines || "";
      f("family").value     = data.family_history || "";
  
      show(view); hide(form);
    }
  
    document.getElementById('editBtn')?.addEventListener('click', () => {
      hide(view); show(form); msg("");
    });
  
    document.getElementById('cancelBtn')?.addEventListener('click', () => {
      show(view); hide(form); msg("Edit canceled");
    });
  
    form?.addEventListener('submit', async (e) => {
      e.preventDefault();
      msg("Saving...");
  
      const payload = {
        symptoms:    f("symptoms").value,
        medications: f("medications").value,
        conditions:  f("conditions").value,
        allergies:   f("allergies").value,
        surgeries:   f("surgeries").value,
        vaccines:    f("vaccines").value,
        family_history: f("family").value
      };
  
      const res = await fetch('/profile/', {
        method: 'PUT',
        headers: { 'Content-Type': 'application/json' },
        credentials: 'same-origin',
        body: JSON.stringify(payload)
      });
      const data = await res.json();
      if (!res.ok || !data.ok) { msg(data.error || "Save failed", "error"); return; }
  
      await loadProfile();  // refresh read-only view with saved values
      msg("Saved.", "ok");
    });
  
    // initial load
    loadProfile().catch(err => msg("Network error", "error"));
  })();
  