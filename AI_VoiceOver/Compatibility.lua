setfenv(1, select(2, ...))

local CLIENT_VERSION = GetBuildInfo()

if not WOW_PROJECT_ID and CLIENT_VERSION == "1.12.1" then

elseif not WOW_PROJECT_ID and CLIENT_VERSION == "3.3.5" then

elseif WOW_PROJECT_ID == WOW_PROJECT_CLASSIC then

elseif WOW_PROJECT_ID == WOW_PROJECT_WRATH_CLASSIC then

    GetGossipText = C_GossipInfo.GetText
    GetNumGossipActiveQuests = C_GossipInfo.GetNumActiveQuests
    GetNumGossipAvailableQuests = C_GossipInfo.GetNumAvailableQuests

    function VoiceOverUtils:getQuestLogScrollOffset()
        return HybridScrollFrame_GetOffset(QuestLogListScrollFrame)
    end

    function VoiceOverUtils:getQuestLogTitleFrame(index)
        return _G["QuestLogListScrollFrameButton" .. index]
    end

    function QuestOverlayUI:updateQuestTitle(questLogTitleFrame, playButton, normalText, questCheck)
        playButton:SetPoint("LEFT", questLogTitleFrame.normalText, "LEFT", 0, 0)
        questLogTitleFrame.normalText:SetText("|TInterface\\Common\\spacer:1:20|t" ..
            (questLogTitleFrame.normalText:GetText() or ""):trim())
        QuestLogTitleButton_Resize(questLogTitleFrame)
    end

    hooksecurefunc(Addon, "OnInitialize", function()
        QuestLogListScrollFrame.update = QuestLog_Update
    end)

elseif WOW_PROJECT_ID == WOW_PROJECT_MAINLINE then

end
