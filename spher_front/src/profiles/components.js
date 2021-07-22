import React from "react";

function UserLink(props) {
  const { username } = props;
  const handleUserLink = (event) => {
    window.location.href = `/profile/${username}`; //? browser api or react
  };
  return (
    <div className="pointer" onClick={handleUserLink}>
      {props.children}
    </div>
  );
}

export function UserDisplay(props) {
  const { user, includeFullName, hideLink } = props;
  const nameDisplay =
    includeFullName === true ? `${user.first_name} ${user.last_name} ` : null;

  return (
    <React.Fragment>
      {nameDisplay}
      {hideLink === true ? (
        `@${user.username}`
      ) : (
        <UserLink username={user.username}>@{user.username}</UserLink>
      )}
    </React.Fragment>
  );
}

export function UserPicture(props) {
  const { user, hideLink } = props;
  const userIdSpan = (
    <span className="mx-1 px-3 py-2 rounded-circle bg-dark text-white">
      {user.username[0]}
    </span>
  );
  return hideLink === true ? (
    userIdSpan
  ) : (
    <UserLink username={user.username}>{userIdSpan}</UserLink>
  );
}
