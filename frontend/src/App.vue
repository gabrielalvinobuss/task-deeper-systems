<template>
  <div id="app">
    <h1>User List</h1>
    <UserList :users="users" @refetch-users="refetchUsers"  />
  </div>
</template>

<script>
import UserList from './components/UserList.vue';

export default {
  components: {
    UserList
  },
  data() {
    return {
      users: []
    };
  },
  methods: {
    refetchUsers() {
        fetch('http://127.0.0.1:5000/api/users')
          .then(response => response.json())
          .then(data => {
            this.users = data;
          })
          .catch(error => {
            console.error('Error finding users:', error);
          });
      }
    },
  mounted() {
    fetch('http://127.0.0.1:5000/api/users')
      .then(response => response.json())
      .then(data => {
        this.users = data;
      })
      .catch(error => {
        console.error('Error finding users:', error);
      });
  }
};
</script>

<style>

</style>