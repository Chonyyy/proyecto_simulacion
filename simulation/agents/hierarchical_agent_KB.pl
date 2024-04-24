%---------------------------- Knowledge -----------------------------------------------


work_is_open(WorkId):-
    not(week_day(saturday)),
    not(week_day(sunday)),
    hour(H),
    open_hours_place(WorkId,I,F),
    open_place(WorkId, true),
    H >= I,
    H =< F.


%---------------------------- Patterns of Behaviour -----------------------------------------------


% check_goals():-
%     ((location(Id), goal(move, Id)) ->
%         (retractall(goal(move, Id)))
%     );
%     ((goal(work), hour(H), work_place(WorkId, _), open_hours_place(WorkId,_,F), H >= F) ->
%         retractall(goal(work)));

%     (goal(wear_mask), wearing_mask(true) ->
%         retractall(goal(wear_mask)));

%     ((goal(medical_check), location(Id), open_hours_place(Id,_,C), hour(H), C == H) ->
%         retractall(goal(medical_check)));

%     ((goal(have_fun),  location(Id), open_hours_place(Id,_,C), hour(H), C == H)  ->
%         retractall(goal(wear_mask)));

%     (goal(remove_mask), wearing_mask(false) ->
%         retractall(goal(remove_mask)));
%     true.

% move(NodeId, Action, Arguments):-
%     social_distancing(SocialDistancing),
%     Action = move,
%     Arguments = [NodeId, SocialDistancing].

% work(Action, Arguments):-
%     Action = work,
%     Arguments = [].

% wear_mask(Action, Arguments):-
%     Action = wear_mask,
%     Arguments = [].

% remove_mask(Action, Arguments):-
%     Action = remove_mask,
%     Arguments = [].
    
% behavioral_step(Action, Arguments, Location, Goal, Mask_necessity, Mask_requirement):-
%     % scheduling
%     % check_schedule(),
    
%     % check archieved goals
%     % check_goals(),
%     % (preconditions) - (actions)
%     (Goal == wear_mask, Mask_necessity == true, mask_requirement(Location, true), wearing_mask(false)->%[X]
%         wear_mask(Action, Arguments));
    
%     (goal(remove_mask), wearing_mask(true)->%[X]
%         remove_mask(Action, Arguments));

%     (goal(work), work_place(Location, _)->
%         work(Action, Arguments));

%     (goal(medical_check)-> Action = medical_check);
%     (goal(move, NodeId)-> %, not(location(NodeId))
%         (move(NodeId, Action, Arguments))).

%     % check archieved goals


%---------------------------- Local Plans --------------------------------------------------------


% Rules

% check_schedule():-
%     hour(H),
%     min(M),
%     (schedule(remove, GoalType, H, M) ->
%         % retractall(goal(GoalType)), retractall(schedule(remove, GoalType, H, M))),
%     (schedule(add, GoalType, H, M) ->
%         % assert(goal(GoalType)), retractall(schedule(add, GoalType, H, M)));
%     (schedule(add, GoalType, Param, H, M) ->
%         % assert(goal(GoalType, Param)), retractall(schedule(add, GoalType, H, M)));
%     true.


goal_move(TagetNode):-
    retractall(goal(move, _)).
    % assert(goal(move, TagetNode)).
    
get_to_work(WorkId):-
    goal_move(WorkId),
    location(WorkId).

get_to_public_place(Id):-
    goal_move(Id),
    location(Id).

get_to_hospital(Hospital):-
    goal_move(Hospital),
    location(Hospital).

work(WorkId):-
    hour(H),
    open_hours_place(WorkId, _, C),
    (not(goal(work))->
        % assert(goal(work)); true),
    H >= C.

medical_check(HospitalId):-
    hour(H),
    open_hours_place(HospitalId, _, C),
    (not(goal(medical_check))->
        % assert(goal(medical_check)); true),
    H >= C.

have_fun(Id):-
    hour(H),
    open_hours_place(Id, _, C),
    (not(goal(have_fun))->
        % assert(goal(have_fun)); true),
    H >= C.

go_home(HomeId):-
    goal_move(HomeId).

work_day_routine(WorkId):-
    home(HomeId),
    get_to_work(WorkId),
    work(WorkId),
    go_home(HomeId).

hospital_rutine(HospitalId):-
    home(HomeId),
    get_to_hospital(HospitalId),
    medical_check(HospitalId),
    go_home(HomeId).

go_public_place_rutine(Id):-
    home(HomeId),
    get_to_public_place(Id),
    have_fun(Id),
    go_home(HomeId).

planification_step(Plan):-
    remove_goals(),
    work_place(WorkId, _),
    ((too_sick(true), hospital(Id,_), open_place(Id, true), hospital_overrun(Id, false))-> hospital_rutine(Id), Plan = hospital_rutine(Id));
    ((work_is_open(WorkId), too_sick(false)) -> work_day_routine(WorkId), Plan = work_day_routine(WorkId));
    ((public_space(Id, _),open_place(Id, true), go_public_place_rutine(Id)); 
    Plan = no_pweek_day(W), (W == saturday; W == sunday)) -> go_public_place_rutine(Id), Plan = lan.


%---------------------------- Cooperation Knowledge -----------------------------------------------


% % Enviar un mensaje
% recibe_message(SenderId, ReceiverId, Message) :-
%     retractall(message(SenderId, Message)),
%     assert(message(SenderId, Message)).

% % Coordinar acciones
% coordinate_action(AgentId, OtherAgentId, PlanId) :-
%     send_message(AgentId, OtherAgentId, coordinate_action),
%     receive_message(AgentId, OtherAgentId, coordinate_action).

% cooperation_step(Plan):- 
%     open_place(PlaceId, true),
%     home(Home),
%     go_public_place_rutine(PlaceId, Home).


%--------------------------- Auxiliary Methods -----------------------------------------


% cooperation_step(Plan)