import session from "./session"

/*
 * @param {String} type One of the constants appearing at the top if this file, e.g. 'UPDATE'
 * @param {String} resource Name of the resource to fetch, e.g. 'posts'
 * @param {Object} params The data request params, depending on the type
 * @returns {Object} { url, options } The HTTP request parameters
 */
function convertDataRequestToHTTP(type, resource, params) {
  let url = '';
  const options = {};

  switch (type) {
    case GET_LIST:
      const { page, perPage } = params.pagination;
      const { field, order } = params.sort;
      const query = {
        sort: JSON.stringify([field, order]),
        range: JSON.stringify([
          (page - 1) * perPage,
          page * perPage - 1,
        ]),
        filter: JSON.stringify(params.filter),
      };
      url = `${resource}?${stringify(query)}`;
      break;

    case GET_ONE:
      url = `${resource}/${params.id}`;
      break;

    case GET_MANY:
      const query = {
        filter: JSON.stringify({ id: params.ids }),
      };
      url = `${resource}?${stringify(query)}`;
      break;

    case GET_MANY_REFERENCE:
      const { page, perPage } = params.pagination;
      const { field, order } = params.sort;
      const query = {
        sort: JSON.stringify([field, order]),
        range: JSON.stringify([
          (page - 1) * perPage,
          page * perPage - 1,
        ]),
        filter: JSON.stringify({
          ...params.filter,
          [params.target]: params.id,
        }),
      };
      url = `${resource}?${stringify(query)}`;
      break;

    case UPDATE:
      url = `${resource}/${params.id}`;
      options.method = 'PUT';
      options.body = JSON.stringify(params.data);
      break;

    case CREATE:
      url = `${resource}`;
      options.method = 'POST';
      options.body = JSON.stringify(params.data);
      break;

    case DELETE:
      url = `${resource}/${params.id}`;
      options.method = 'DELETE';
      break;

    default:
      throw new Error(`Unsupported fetch action type ${type}`);
  }
  return { url, options };
}

/*
 * @param {string} type Request type, e.g GET_LIST
 * @param {string} resource Resource name, e.g. "posts"
 * @param {Object} payload Request parameters. Depends on the request type
 * @returns {Promise} the Promise for a data response
 *
 * @example
 * GET_LIST     => GET http://my.api.url/posts?sort=['title','ASC']&range=[0, 24]
 * GET_ONE      => GET http://my.api.url/posts/123
 * GET_MANY     => GET http://my.api.url/posts?filter={ids:[123,456,789]}
 * UPDATE       => PUT http://my.api.url/posts/123
 * CREATE       => POST http://my.api.url/posts
 * DELETE       => DELETE http://my.api.url/posts/123
 */
function request(type, resource, params) => {
  const { url, options } = convertDataRequestToHTTP(
    type,
    resource,
    params
  );

  return session({
    method: options.method,
    url,
    data: options.body,
  })
}

export default request;
