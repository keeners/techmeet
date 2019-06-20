import session from "./session"

export default {
  /*
   * Users
   */
  getUsers() {
    return session.get("/api/users/")
  },

  /*
   * Techgroups
   */
  getTechgroups() {
    return session.get("/api/techgroups/")
  },

  /*
   * Events
   */
  getEvents() {
    return session.get("/api/events/")
  },

  /*
   * Members
   */
  getMembers() {
    return session.get("/api/members/")
  },
}
