# Plan pracy — WAO-AI

## Status audytu
AUDYT ZAKOŃCZONY — 2026-09-12.

## Stan faktyczny
Warstwowa architektura agenta operacyjnego: normalizacja CTCO, planowanie, polityka wykonania, weryfikacja, synteza, warstwa bezpieczeństwa, MCP, REST, ChatGPT Apps SDK oraz obserwowalność. README wyraźnie rozdziela dane wejściowe od instrukcji nadrzędnych i opisuje anti-prompt-injection.

## Ryzyka
- agent może wykonywać narzędzia o skutkach zewnętrznych;
- potrzebna jest realna autoryzacja, nie tylko dokumentacyjna polityka;
- MCP/REST muszą mieć spójne auth, rate limits i audyt;
- telemetryka może zawierać dane wrażliwe.

## Priorytet
KRYTYCZNY.

## Kolejność prac
1. Zmapować implementację core/safety/tools/interfaces.
2. Zweryfikować policy enforcement w runtime.
3. Przetestować prepared/authorized/executed jako rozdzielne stany.
4. Zweryfikować auth, RBAC, secrets i rate limits.
5. Dodać testy prompt injection, tool trust i side effects.
6. Przeprowadzić testy kontraktowe REST/MCP.
7. Spolonizować dokumentację i przygotować rebranding.

## Kryterium zakończenia
Granice bezpieczeństwa są wymuszalne w kodzie, nie tylko opisane w README; testy potwierdzają fail-closed dla działań wymagających autoryzacji.
