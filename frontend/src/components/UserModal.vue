<template>
  <div>
    <Dialog header="User Form" :visible="showModal" modal >
      <form @submit.prevent="saveUser">
        <div class="p-field">
          <label for="username">Username</label>
          <InputText id="username" v-model="user.username" required disabled />
        </div>
        <div class="p-field">
          <label for="roles">Roles</label>
          <InputText id="roles" v-model="user.roles" required />
        </div>
        <div class="p-field">
          <label for="timezone">Timezone</label>
          <InputText id="timezone" v-model="user.preferences.timezone" required />
        </div>
        <div class="p-field">
          <label for="active">Active</label>
          <Checkbox v-model="user.active" id="active" binary />
        </div>
        <div class="p-field">
          <Button label="Save" type="submit" />
          <Button label="Cancel" class="p-button-secondary" @click="cancel" />
        </div>
      </form>
    </Dialog>
  </div>
</template>

<script>
import { ref, watch } from "vue";
import Dialog from "primevue/dialog";
import InputText from "primevue/inputtext";
import Checkbox from "primevue/checkbox";
import Button from "primevue/button";

export default {
  name: "UserModal",
  components: {
    Dialog,
    InputText,
    Checkbox,
    Button,
  },
  props: {
    showModal: Boolean,
    currentUser: Object,
  },
  setup(props, { emit }) {
    const user = ref({ ...props.currentUser });
    
    watch(() => props.currentUser, (newValue) => {
      user.value = { ...newValue };
    });

    const resetForm = () => {
      user.value = { username: "", roles: "", preferences: { timezone: "" }, active: true };
      console.log("resetForm");
    };

    const saveUser = () => {
      emit("save-user", user.value);
      resetForm();
    };

    const cancel = () => {
      emit("close-modal");
      resetForm();
    };

    return {
      user,
      resetForm,
      saveUser,
      cancel
    };
  }
};
</script>

<style scoped>
/* Estilo adicional para o modal */
.p-field {
  margin-bottom: 1em;
}
</style>
