<template>
  <div>
    <Button label="Create New User" icon="pi pi-plus" @click="openCreateModal" />
    
    <Datatable :value="users">
      <Column field="username" header="Username"></Column>
      <Column field="active" header="Active"></Column>
      <Column field="preferences.timezone" header="Timezone"></Column>
      <Column header="Actions">
        <template #body="slotProps">
          <div class="flex gap-2">
            <Button label="Edit" icon="pi pi-pencil" @click="openEditModal(slotProps.rowData)" />
            <Button label="Delete" icon="pi pi-trash" @click="deleteUser(slotProps.rowData.username)" />
          </div>
        </template>
      </Column>
    </Datatable>

    <UserModal
      :showModal="showModal"
      :currentUser="currentUser"
      @save-user="saveUser"
      @close-modal="closeModal"
    />
  </div>
</template>

<script>
import { ref } from "vue";
import Button from "primevue/button";
import UserModal from "./UserModal.vue";
import Datatable from "primevue/datatable";
import Column from "primevue/column";

export default {
  name: "UserList",
  components: {
    Button,
    UserModal,
    Datatable,
    Column,
  },
  props: {
    users: Array
  },
  setup(props, { emit }) {
    const showModal = ref(false);
    const currentUser = ref(null);

    const openCreateModal = () => {
      currentUser.value = { username: "", roles: "", preferences: { timezone: "" }, active: true };
      showModal.value = true;
    };

    const openEditModal = (user) => {
      currentUser.value = { ...user };
      showModal.value = true;
    };

    const closeModal = () => {
      showModal.value = false;
    };

    const saveUser = async (user) => {
        try {
            const method = user._id ? "PUT" : "POST";
            const url = user._id
            ? `http://127.0.0.1:5000/api/users/${user.username}`
            : "http://127.0.0.1:5000/api/users";

            const response = await fetch(url, {
            method: method,
            headers: {
                "Content-Type": "application/json",
            },
            body: JSON.stringify({
                username: user.username,
                roles: user.roles,
                preferences: user.preferences,
                active: user.active,
            }),
            });

            if (response.ok) {
            alert("User saved successfully!");
            closeModal();
            emit("refetch-users");
            } else {
            alert("Error saving user");
            }
        } catch (error) {
            console.error("Error saving user:", error);
        }
    };

    const deleteUser = async (username) => {
      if (confirm(`Are you sure you want to delete ${username}?`)) {
        try {
          const response = await fetch(`http://127.0.0.1:5000/api/users/${username}`, {
            method: "DELETE",
          });
          if (response.ok) {
            alert(`User ${username} deleted successfully!`);
            emit("refetch-users");
          } else {
            alert(`Error deleting user ${username}`);
          }
        } catch (error) {
          console.error("Error deleting user:", error);
        }
      }
    };

    return {
      showModal,
      currentUser,
      openCreateModal,
      openEditModal,
      closeModal,
      saveUser,
      deleteUser
    };
  }
};
</script>

<style scoped>
/* Estilo para a tabela */
table {
  width: 100%;
  border-collapse: collapse;
}
th, td {
  padding: 8px;
  text-align: left;
  border: 1px solid #ddd;
}
th {
  background-color: #f4f4f4;
}
</style>
