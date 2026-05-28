def run_episode(env, policy=None, seed=0, max_steps=200, verbose=True):
    """Executa um único episódio. Retorna (total_reward, n_steps, last_info)."""
    obs, info = env.reset(seed=seed)
    env.action_space.seed(seed)
    if policy is None:
        policy = lambda o: env.action_space.sample()   # política aleatória

    total_reward, steps = 0.0, 0
    terminated = truncated = False
    while not (terminated or truncated):
        obs, reward, terminated, truncated, info = env.step(policy(obs))
        total_reward += reward
        steps += 1
        if steps >= max_steps:
            break

    if verbose:
        print(f"steps={steps:3d}  total_reward={total_reward:8.3f}  "
              f"terminated={terminated}  truncated={truncated}")
    return total_reward, steps, info

def make_scripted(path):
    """Cria uma política com estado que executa uma lista fixa de ações.

    Após consumir todas as ações da lista, a política passa a ficar parada.
    """
    cursor = {"i": 0}
    def policy(obs):
        i = cursor["i"]
        cursor["i"] += 1
        return path[i] if i < len(path) else 0
    return policy

