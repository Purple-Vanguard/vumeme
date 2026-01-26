#!/usr/bin/env bash
set -euo pipefail

if [ -f "Makefile" ] && make -n test >/dev/null 2>&1; then
  make test
  exit 0
fi

if [ -f "package.json" ]; then
  npm ci
  npm test
  exit 0
fi

echo "No CI command configured. Add Makefile:test or package.json scripts."
exit 1
