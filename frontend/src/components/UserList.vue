<template>
  <div>
    <Button label="Create New User" icon="pi pi-plus" @click="openCreateModal" />
    <table>
      <thead>
        <tr>
          <th>Username</th>
          <th>Roles</th>
          <th>Active</th>
          <th>Timezone</th>
          <th>Actions</th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="user in users" :key="user._id">
          <td>{{ user.username }}</td>
          <!-- <td>{{ user.roles.join(", ") }}</td> -->
          <td>{{ user.active ? "Yes" : "No" }}</td>
          <td>{{ user.preferences.timezone }}</td>
          <td>
            <Button label="Edit" icon="pi pi-pencil" @click="openEditModal(user)" />
            <Button label="Delete" icon="pi pi-trash" @click="deleteUser(user.username)" />
          </td>
        </tr>
      </tbody>
    </table>

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

export default {
  name: "UserList",
  components: {
    Button,
    UserModal,
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
            body: JSON.stringify(user),
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
