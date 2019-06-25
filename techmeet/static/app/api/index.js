import session from "./session"

export default {
  /*
   * Users
   */
  getUsers() {
    return session.get("/api/users/")
  },
  getUser({id}) {
    return session.get(`/api/users/${id}/`)
  },

  /*
   * Techgroups
   */
  getTechgroups() {
    return session.get("/api/techgroups/")
  },
  getTechgroup({id}) {
    return session.get(`/api/techgroups/${id}/`)
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
